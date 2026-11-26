from datetime import date, timedelta, datetime
from collections import Counter
import calendar
import csv
import json
import shutil
from pathlib import Path

DATA_FILE = Path("habits.json")
BACKUP_DIR = Path("backups")
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def empty_data():
    return {
        "settings": {"streak_freeze_enabled": False},
        "habits": {}
    }


def create_startup_backup():
    if DATA_FILE.exists():
        try:
            BACKUP_DIR.mkdir(exist_ok=True)
            stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
            backup_path = BACKUP_DIR / f"habits_{stamp}.json"
            shutil.copy2(DATA_FILE, backup_path)
            print(f"Backup created: {backup_path}")
        except OSError as error:
            print(f"Could not create startup backup: {error}")


def load_data():
    if not DATA_FILE.exists():
        print("No saved data found. Starting with an empty tracker.")
        return empty_data()

    try:
        raw = DATA_FILE.read_text(encoding="utf-8")
        if not raw.strip():
            print("The data file is empty. Starting with an empty tracker.")
            return empty_data()

        loaded = json.loads(raw)
        if not isinstance(loaded, dict) or not isinstance(loaded.get("habits", {}), dict):
            raise ValueError("The JSON structure is not a valid habit tracker file.")

        result = empty_data()
        settings = loaded.get("settings", {})
        if isinstance(settings, dict):
            result["settings"]["streak_freeze_enabled"] = bool(
                settings.get("streak_freeze_enabled", False)
            )

        for name, record in loaded.get("habits", {}).items():
            if not isinstance(name, str) or not isinstance(record, dict):
                continue
            try:
                created_on = date.fromisoformat(record.get("created_on", date.today().isoformat())).isoformat()
            except (TypeError, ValueError):
                created_on = date.today().isoformat()

            done_dates = record.get("done_dates", [])
            if not isinstance(done_dates, list):
                done_dates = []
            valid_dates = []
            for item in done_dates:
                try:
                    valid_dates.append(date.fromisoformat(item).isoformat())
                except (TypeError, ValueError):
                    continue

            target = record.get("target_per_week", 5)
            if not isinstance(target, int) or not 1 <= target <= 7:
                target = 5

            result["habits"][name] = {
                "created_on": created_on,
                "target_per_week": target,
                "done_dates": sorted(set(valid_dates))
            }

        print("Saved data loaded successfully.")
        return result

    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"Could not read the data file ({error}). Starting with an empty tracker.")
        print("The original file has not been changed; its startup backup, if created, is in the backups folder.")
        return empty_data()


def save_data():
    try:
        DATA_FILE.write_text(json.dumps(data, indent=4), encoding="utf-8")
    except OSError as error:
        print(f"Could not save data: {error}")


def get_habit_names():
    return list(data["habits"].keys())


def choose_habit(prompt="Choose a habit number (0 to cancel): "):
    names = get_habit_names()
    if not names:
        print("There are no habits yet.")
        return None

    for number, name in enumerate(names, start=1):
        print(f"{number}. {name}")

    while True:
        raw = input(prompt).strip()
        try:
            number = int(raw)
        except ValueError:
            print("Enter a valid number.")
            continue

        if number == 0:
            return None
        if 1 <= number <= len(names):
            return names[number - 1]
        print("That habit number does not exist.")


def ask_target():
    while True:
        raw = input("Target days per week (1-7): ").strip()
        try:
            target = int(raw)
        except ValueError:
            print("Enter a whole number from 1 to 7.")
            continue
        if 1 <= target <= 7:
            return target
        print("The target must be between 1 and 7.")


def add_habit():
    while True:
        name = input("New habit name: ").strip()
        if not name:
            print("Habit name cannot be empty.")
            continue
        if any(name.casefold() == existing.casefold() for existing in data["habits"]):
            print("That habit already exists.")
            continue
        break

    target = ask_target()
    data["habits"][name] = {
        "created_on": date.today().isoformat(),
        "target_per_week": target,
        "done_dates": []
    }
    save_data()
    print(f"'{name}' added.")


def rename_habit():
    old_name = choose_habit()
    if old_name is None:
        return

    while True:
        new_name = input("New name: ").strip()
        if not new_name:
            print("Habit name cannot be empty.")
            continue
        if any(new_name.casefold() == name.casefold() for name in data["habits"] if name != old_name):
            print("Another habit already uses that name.")
            continue
        break

    rebuilt = {}
    for name, record in data["habits"].items():
        rebuilt[new_name if name == old_name else name] = record
    data["habits"] = rebuilt
    save_data()
    print(f"'{old_name}' renamed to '{new_name}'.")


def remove_habit():
    name = choose_habit()
    if name is None:
        return
    answer = input(f"Remove '{name}'? (y/n): ").strip().lower()
    if answer == "y":
        del data["habits"][name]
        save_data()
        print("Habit removed.")
    else:
        print("Removal cancelled.")


def ask_completion_date(record):
    while True:
        raw = input("Completion date (YYYY-MM-DD, or Enter for today): ").strip()
        if not raw:
            chosen = date.today()
        else:
            try:
                chosen = date.fromisoformat(raw)
                if chosen.isoformat() != raw:
                    raise ValueError
            except ValueError:
                print("Use a valid date in YYYY-MM-DD format.")
                continue

        if chosen > date.today():
            print("Future dates cannot be recorded.")
            continue
        if chosen < date.fromisoformat(record["created_on"]):
            print("You cannot record a completion before this habit was created.")
            continue
        return chosen


def mark_habit_done():
    name = choose_habit()
    if name is None:
        return

    record = data["habits"][name]
    chosen = ask_completion_date(record)
    chosen_text = chosen.isoformat()

    if chosen_text in record["done_dates"]:
        print("That habit is already marked done for this date.")
        return

    record["done_dates"].append(chosen_text)
    record["done_dates"].sort()
    save_data()
    print(f"'{name}' marked done for {chosen_text}.")


def streak_values(record, freeze_enabled):
    """Return (current_streak, longest_streak); a freeze day counts as a streak day."""
    today = date.today()
    completed = {date.fromisoformat(item) for item in record["done_dates"]}
    created = date.fromisoformat(record["created_on"])

    # Do not treat an unfinished today as a missed day yet.
    end_day = today if today in completed else today - timedelta(days=1)
    if end_day < created:
        return 0, 0

    current = 0
    longest = 0
    frozen_weeks = set()
    day = created

    while day <= end_day:
        week_start = day - timedelta(days=day.weekday())

        if day in completed:
            current += 1
        elif freeze_enabled and current > 0 and week_start not in frozen_weeks:
            # One missed day in this Monday-Sunday week is protected.
            frozen_weeks.add(week_start)
            current += 1
        else:
            current = 0

        longest = max(longest, current)
        day += timedelta(days=1)

    return current, longest


def active_period_start(record, days):
    today = date.today()
    first_day = today - timedelta(days=days - 1)
    created = date.fromisoformat(record["created_on"])
    return max(first_day, created)


def completion_rate(record, days):
    start = active_period_start(record, days)
    today = date.today()
    active_days = (today - start).days + 1
    completed = {
        date.fromisoformat(item)
        for item in record["done_dates"]
        if start <= date.fromisoformat(item) <= today
    }
    return (len(completed) / active_days * 100) if active_days > 0 else 0.0



def missed_days_since_creation(record):
    """Count missed days only through the last completed day, not an unfinished today."""
    today = date.today()
    created = date.fromisoformat(record["created_on"])
    done = set(record["done_dates"])
    last_day = today if today.isoformat() in done else today - timedelta(days=1)
    if last_day < created:
        return 0
    elapsed_days = (last_day - created).days + 1
    completed_count = sum(
        1 for item in done
        if created <= date.fromisoformat(item) <= last_day
    )
    return max(0, elapsed_days - completed_count)

def current_week_dates():
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    return [monday + timedelta(days=offset) for offset in range(7)]


def show_habits():
    today = date.today()
    freeze = data["settings"]["streak_freeze_enabled"]
    print(f"\nToday: {today.strftime('%a %d %b %Y')}")
    print(f"Streak freeze: {'ON' if freeze else 'OFF'}\n")
    print(f"{'Habit':<23} {'Today':<7} {'Streak':<9} {'7-day rate':<11} {'30-day':<9} {'Target'}")
    print("-" * 78)

    for name, record in sorted(
        data["habits"].items(),
        key=lambda item: streak_values(item[1], freeze)[0],
        reverse=True
    ):
        done_today = today.isoformat() in record["done_dates"]
        current, _ = streak_values(record, freeze)
        rate7 = completion_rate(record, 7)
        rate30 = completion_rate(record, 30)
        week_done = sum(
            day.isoformat() in record["done_dates"]
            for day in current_week_dates()
            if day <= today
        )
        target_status = "Met" if week_done >= record["target_per_week"] else f"{week_done}/{record['target_per_week']}"
        print(
            f"{name:<23} {'[x]' if done_today else '[ ]':<7} "
            f"{current:<9} {rate7:>6.1f}%     {rate30:>6.1f}%   {target_status}"
        )


def show_weekly_summary():
    days = current_week_dates()
    print("\nWeekly summary (Monday to Sunday)")
    print(f"{'Habit':<22} " + " ".join(WEEKDAYS))
    print("-" * 52)
    for name, record in data["habits"].items():
        marks = ["x" if day.isoformat() in record["done_dates"] else "-" for day in days]
        completed_this_week = sum(mark == "x" for mark in marks)
        target_met = "Met" if completed_this_week >= record["target_per_week"] else "Not met"
        print(f"{name:<22} " + "  ".join(marks) + f"   {completed_this_week}/{record['target_per_week']} ({target_met})")


def show_month_calendar():
    while True:
        raw = input("Enter month to view (YYYY-MM): ").strip()
        try:
            year_text, month_text = raw.split("-")
            year, month = int(year_text), int(month_text)
            if len(year_text) != 4 or not 1 <= month <= 12:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid month in YYYY-MM format.")

    print(f"\n{calendar.month_name[month]} {year}")
    print("Mon Tue Wed Thu Fri Sat Sun")
    month_grid = calendar.monthcalendar(year, month)

    for week in month_grid:
        cells = []
        for day_number in week:
            if day_number == 0:
                cells.append("   ")
                continue

            this_day = date(year, month, day_number)
            active_habits = [
                record for record in data["habits"].values()
                if date.fromisoformat(record["created_on"]) <= this_day
            ]
            all_done = bool(active_habits) and all(
                this_day.isoformat() in record["done_dates"]
                for record in active_habits
            )
            marker = "*" if all_done else "-"
            cells.append(f"{day_number:2}{marker}")
        print(" ".join(cells))
    print("* = every habit that existed on that date was completed; - = not all completed.")


def show_insights():
    if not data["habits"]:
        print("Add habits first to see insights.")
        return

    freeze = data["settings"]["streak_freeze_enabled"]
    consistency = {}
    missed_days = {}
    print("\nHabit insights")

    for name, record in data["habits"].items():
        counts = Counter(
            date.fromisoformat(item).strftime("%A")
            for item in record["done_dates"]
        )
        if counts:
            highest = max(counts.values())
            best_days = [day for day, count in counts.items() if count == highest]
            weekday_text = ", ".join(best_days)
        else:
            weekday_text = "No completions yet"
        print(f"{name}: most-completed weekday: {weekday_text}")

        consistency[name] = completion_rate(record, 30)
        missed_days[name] = missed_days_since_creation(record)

    most_consistent = max(consistency, key=consistency.get)
    most_missed = max(missed_days, key=missed_days.get)
    print(f"\nMost consistent (30-day rate): {most_consistent} ({consistency[most_consistent]:.1f}%)")
    print(f"Most missed days since creation: {most_missed} ({missed_days[most_missed]} days)")


def export_csv():
    filename = input("CSV filename (press Enter for habit_report.csv): ").strip()
    if not filename:
        filename = "habit_report.csv"
    if not filename.lower().endswith(".csv"):
        filename += ".csv"

    freeze = data["settings"]["streak_freeze_enabled"]
    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Habit", "Created On", "Target Per Week", "Completed Dates",
                "Current Streak", "Longest Streak", "7-Day Rate (%)",
                "30-Day Rate (%)", "Missed Days Since Creation"
            ])
            for name, record in data["habits"].items():
                current, longest = streak_values(record, freeze)
                writer.writerow([
                    name, record["created_on"], record["target_per_week"],
                    "; ".join(record["done_dates"]), current, longest,
                    round(completion_rate(record, 7), 1),
                    round(completion_rate(record, 30), 1),
                    missed_days_since_creation(record)
                ])
        print(f"Report exported to {filename}.")
    except OSError as error:
        print(f"Could not export CSV: {error}")


def settings_menu():
    current = data["settings"]["streak_freeze_enabled"]
    print(f"\nStreak freeze is currently {'ON' if current else 'OFF'}.")
    answer = input("Toggle it? (y/n): ").strip().lower()
    if answer == "y":
        data["settings"]["streak_freeze_enabled"] = not current
        save_data()
        print(f"Streak freeze is now {'ON' if not current else 'OFF'}.")


def show_pending_habits():
    today_text = date.today().isoformat()
    freeze = data["settings"]["streak_freeze_enabled"]
    pending = [
        (name, record) for name, record in data["habits"].items()
        if today_text not in record["done_dates"]
    ]
    pending.sort(key=lambda item: streak_values(item[1], freeze)[0], reverse=True)

    print("\nHabits still to complete today (highest streak first):")
    if not pending:
        print("All habits are completed today. Great work!")
        return
    for name, record in pending:
        current, _ = streak_values(record, freeze)
        print(f"- {name} ({current}-day streak)")


def main():
    global data
    create_startup_backup()
    data = load_data()
    show_pending_habits()

    while True:
        print("\n===== HABIT TRACKER =====")
        print("1. Add habit")
        print("2. Rename habit")
        print("3. Remove habit")
        print("4. Mark habit done (today or past date)")
        print("5. Show habit dashboard")
        print("6. Weekly summary")
        print("7. Monthly calendar")
        print("8. Insights")
        print("9. Export CSV report")
        print("10. Settings (streak freeze)")
        print("11. Exit")

        choice = input("Menu choice: ").strip()
        if choice == "1":
            add_habit()
        elif choice == "2":
            rename_habit()
        elif choice == "3":
            remove_habit()
        elif choice == "4":
            mark_habit_done()
        elif choice == "5":
            show_habits()
        elif choice == "6":
            show_weekly_summary()
        elif choice == "7":
            show_month_calendar()
        elif choice == "8":
            show_insights()
        elif choice == "9":
            export_csv()
        elif choice == "10":
            settings_menu()
        elif choice == "11":
            save_data()
            print("Data saved. Goodbye!")
            break
        else:
            print("Invalid choice. Select 1-11.")


if __name__ == "__main__":
    main()
