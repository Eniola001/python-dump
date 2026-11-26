"""A beginner-friendly command-line habit tracker (Project Levels 1-4).

The program stores habits in habits.json beside this script. It uses only
Python's standard library; no extra packages need to be installed.
"""

from datetime import date, datetime, timedelta
from collections import Counter
from pathlib import Path
import calendar
import csv
import json
import shutil


# Keep the data and report files beside this Python file.
FOLDER = Path(__file__).resolve().parent
DATA_FILE = FOLDER / "habits.json"
BACKUP_FOLDER = FOLDER / "backups"
CSV_FILE = FOLDER / "habit_report.csv"
WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


def empty_data():
    """Create the starting structure for a new tracker."""
    return {
        "settings": {"streak_freeze_enabled": False},
        "habits": {}
    }


def parse_date(value):
    """Return a date for an exact YYYY-MM-DD string, or None if invalid."""
    if not isinstance(value, str):
        return None
    try:
        result = date.fromisoformat(value)
    except ValueError:
        return None
    return result if result.isoformat() == value else None


# ----------------------------- LEVEL 3: FILES -----------------------------

def create_startup_backup():
    """Back up the existing JSON file before loading it."""
    if not DATA_FILE.exists():
        return

    try:
        BACKUP_FOLDER.mkdir(exist_ok=True)
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        backup_file = BACKUP_FOLDER / f"habits_{stamp}.json"
        shutil.copy2(DATA_FILE, backup_file)
        print(f"Backup created: {backup_file.name}")
    except OSError as error:
        print(f"Warning: backup could not be created: {error}")


def load_data():
    """Load habits safely; use an empty tracker if the file is unavailable."""
    if not DATA_FILE.exists():
        print("No saved data found. Starting a new tracker.")
        return empty_data()

    try:
        text = DATA_FILE.read_text(encoding="utf-8")
        if not text.strip():
            print("The data file is empty. Starting a new tracker.")
            return empty_data()

        saved = json.loads(text)
        if not isinstance(saved, dict) or not isinstance(saved.get("habits"), dict):
            raise ValueError("The file does not contain the expected habit data.")

        result = empty_data()
        settings = saved.get("settings", {})
        if isinstance(settings, dict):
            result["settings"]["streak_freeze_enabled"] = (
                settings.get("streak_freeze_enabled") is True
            )

        today = date.today()
        used_names = set()

        for name, record in saved["habits"].items():
            if not isinstance(name, str) or not name.strip() or not isinstance(record, dict):
                continue

            name = name.strip()
            if name.casefold() in used_names:
                continue

            created = parse_date(record.get("created_on")) or today
            if created > today:
                created = today

            target = record.get("target_per_week", 5)
            if isinstance(target, bool) or not isinstance(target, int) or not 1 <= target <= 7:
                target = 5

            dates = record.get("done_dates", [])
            if not isinstance(dates, list):
                dates = []

            clean_dates = set()
            for item in dates:
                completed = parse_date(item)
                if completed and created <= completed <= today:
                    clean_dates.add(completed.isoformat())

            result["habits"][name] = {
                "created_on": created.isoformat(),
                "target_per_week": target,
                "done_dates": sorted(clean_dates)
            }
            used_names.add(name.casefold())

        print("Saved habits loaded successfully.")
        return result

    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, TypeError) as error:
        print(f"Could not load the saved data: {error}")
        print("Starting with an empty tracker. The original file has not been changed.")
        return empty_data()


def save_data(data):
    """Save through a temporary file so an interrupted save is less risky."""
    temporary_file = DATA_FILE.with_name(DATA_FILE.name + ".tmp")
    try:
        temporary_file.write_text(json.dumps(data, indent=4), encoding="utf-8")
        temporary_file.replace(DATA_FILE)
        return True
    except OSError as error:
        print(f"Could not save data: {error}")
        print("The changes remain in memory but may be lost when the program closes.")
        return False


# ----------------------------- LEVEL 1: BASICS ----------------------------

def add_habit(data):
    """Add a habit and its starting information."""
    while True:
        name = input("Habit name: ").strip()
        if not name:
            print("A habit name cannot be empty.")
            continue
        if any(name.casefold() == old.casefold() for old in data["habits"]):
            print("That habit already exists.")
            continue
        break

    target = ask_target()
    data["habits"][name] = {
        "created_on": date.today().isoformat(),
        "target_per_week": target,
        "done_dates": []
    }
    if save_data(data):
        print(f"'{name}' was added.")


def ask_target():
    """Get a whole-number weekly target from 1 to 7."""
    while True:
        answer = input("Target days per week (1-7): ").strip()
        try:
            target = int(answer)
        except ValueError:
            print("Enter a whole number from 1 to 7.")
            continue
        if 1 <= target <= 7:
            return target
        print("The target must be between 1 and 7.")


def choose_habit(data):
    """Show numbered habits and return the chosen name; 0 cancels."""
    names = list(data["habits"])
    if not names:
        print("There are no habits yet. Add one first.")
        return None

    print("\nHabits:")
    for number, name in enumerate(names, start=1):
        print(f"{number}. {name}")

    while True:
        answer = input("Choose a habit number (0 to cancel): ").strip()
        try:
            number = int(answer)
        except ValueError:
            print("Enter a whole number.")
            continue
        if number == 0:
            return None
        if 1 <= number <= len(names):
            return names[number - 1]
        print("That habit number is not on the list.")


def ask_completion_date(record):
    """Ask for today or a valid past date within this habit's lifetime."""
    created = date.fromisoformat(record["created_on"])

    while True:
        answer = input("Completion date (YYYY-MM-DD, or Enter for today): ").strip()
        if answer == "":
            chosen = date.today()
        else:
            chosen = parse_date(answer)
            if chosen is None:
                print("Use a valid date in YYYY-MM-DD format.")
                continue

        if chosen > date.today():
            print("Future dates cannot be recorded.")
        elif chosen < created:
            print("You cannot record a date before this habit was created.")
        else:
            return chosen


def mark_habit_done(data):
    """Record one completion for the selected habit and date."""
    name = choose_habit(data)
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
    if save_data(data):
        print(f"'{name}' marked done for {chosen_text}.")


def streak_values(record, freeze_enabled=False):
    """Return the current and longest streak for one habit.

    An unfinished today is not counted as a missed day yet. When streak freeze
    is on, one missed day in each Monday-Sunday week can protect an active streak.
    """
    today = date.today()
    created = date.fromisoformat(record["created_on"])
    completed = {date.fromisoformat(item) for item in record["done_dates"]}

    last_day = today if today in completed else today - timedelta(days=1)
    if last_day < created:
        return 0, 0

    run = 0
    longest = 0
    weeks_with_freeze = set()
    current_day = created

    while current_day <= last_day:
        week_start = current_day - timedelta(days=current_day.weekday())

        if current_day in completed:
            run += 1
        elif freeze_enabled and run > 0 and week_start not in weeks_with_freeze:
            weeks_with_freeze.add(week_start)
            run += 1
        else:
            run = 0

        longest = max(longest, run)
        current_day += timedelta(days=1)

    return run, longest


def show_habits(data):
    """Display today's completion status and current streak for every habit."""
    if not data["habits"]:
        print("No habits to display. Add a habit first.")
        return

    today = date.today()
    today_text = today.isoformat()
    print(f"\nToday: {today.strftime('%a %d %b %Y')}\n")
    print(f"{'Habit':<25} {'Today':<8} {'Streak'}")
    print("-" * 48)

    for number, (name, record) in enumerate(data["habits"].items(), start=1):
        status = "[x]" if today_text in record["done_dates"] else "[ ]"
        current, _ = streak_values(record, data["settings"]["streak_freeze_enabled"])
        print(f"{number}. {name:<22} {status:<8} {current} days")


# ------------------------- LEVEL 2: HABIT MANAGEMENT ----------------------

def rename_habit(data):
    old_name = choose_habit(data)
    if old_name is None:
        return

    while True:
        new_name = input("New habit name: ").strip()
        if not new_name:
            print("A habit name cannot be empty.")
            continue
        duplicate = any(
            new_name.casefold() == name.casefold()
            for name in data["habits"] if name != old_name
        )
        if duplicate:
            print("Another habit already has that name.")
            continue
        break

    renamed = {}
    for name, record in data["habits"].items():
        renamed[new_name if name == old_name else name] = record
    data["habits"] = renamed

    if save_data(data):
        print(f"'{old_name}' was renamed to '{new_name}'.")


def remove_habit(data):
    name = choose_habit(data)
    if name is None:
        return

    answer = input(f"Remove '{name}'? (y/n): ").strip().lower()
    if answer == "y":
        del data["habits"][name]
        if save_data(data):
            print("Habit removed.")
    else:
        print("Removal cancelled.")


def period_stats(record, number_of_days):
    """Return (completed, active, missed, percentage) for the recent period."""
    today = date.today()
    created = date.fromisoformat(record["created_on"])
    first_day = max(created, today - timedelta(days=number_of_days - 1))
    active_days = (today - first_day).days + 1

    completed = {
        date.fromisoformat(item)
        for item in record["done_dates"]
        if first_day <= date.fromisoformat(item) <= today
    }
    completed_count = len(completed)
    missed_count = active_days - completed_count
    percentage = completed_count / active_days * 100 if active_days else 0.0

    return completed_count, active_days, missed_count, percentage


# ------------------------- LEVEL 3: SUMMARIES -----------------------------

def current_week_dates():
    """Return the seven dates from this week's Monday to Sunday."""
    today = date.today()
    monday = today - timedelta(days=today.weekday())
    return [monday + timedelta(days=offset) for offset in range(7)]


def show_dashboard(data):
    """Show streaks, completion rates and weekly target progress."""
    if not data["habits"]:
        print("No habits to display. Add a habit first.")
        return

    today = date.today()
    freeze = data["settings"]["streak_freeze_enabled"]
    print(f"\nToday: {today.strftime('%a %d %b %Y')}")
    print(f"Streak freeze: {'ON' if freeze else 'OFF'}")
    print("\nHabits are sorted by current streak (highest first).\n")
    print(f"{'Habit':<22} {'Today':<7} {'Now':<5} {'Best':<5} {'7-day':<9} {'30-day':<9} {'Target'}")
    print("-" * 75)

    ordered = sorted(
        data["habits"].items(),
        key=lambda item: streak_values(item[1], freeze)[0],
        reverse=True
    )

    for name, record in ordered:
        current, longest = streak_values(record, freeze)
        _, _, _, rate7 = period_stats(record, 7)
        _, _, _, rate30 = period_stats(record, 30)
        done_this_week = sum(
            day.isoformat() in record["done_dates"]
            for day in current_week_dates() if day <= today
        )
        target = "Met" if done_this_week >= record["target_per_week"] else f"{done_this_week}/{record['target_per_week']}"
        status = "[x]" if today.isoformat() in record["done_dates"] else "[ ]"

        print(
            f"{name:<22} {status:<7} {current:<5} {longest:<5} "
            f"{rate7:>6.1f}%   {rate30:>6.1f}%   {target}"
        )


def show_weekly_summary(data):
    """Print an x/- grid for this week; future days remain blank."""
    if not data["habits"]:
        print("No habits to summarise. Add a habit first.")
        return

    days = current_week_dates()
    today = date.today()
    print("\nWeekly summary (Monday to Sunday)")
    print("x = completed, - = missed, blank = a future day\n")
    print(f"{'Habit':<22} " + " ".join(WEEKDAYS) + "   Target")
    print("-" * 65)

    for name, record in data["habits"].items():
        marks = []
        for day in days:
            if day > today:
                marks.append(" ")
            elif day.isoformat() in record["done_dates"]:
                marks.append("x")
            else:
                marks.append("-")

        completed = sum(
            day.isoformat() in record["done_dates"] for day in days if day <= today
        )
        target_status = "Met" if completed >= record["target_per_week"] else "Not met"
        print(
            f"{name:<22} " + "  ".join(marks)
            + f"   {completed}/{record['target_per_week']} ({target_status})"
        )


def show_month_calendar(data):
    """Mark dates when all habits that existed on that date were completed."""
    if not data["habits"]:
        print("Add habits before creating a calendar.")
        return

    while True:
        answer = input("Month to display (YYYY-MM): ").strip()
        try:
            if len(answer) != 7 or answer[4] != "-":
                raise ValueError
            year = int(answer[:4])
            month = int(answer[5:])
            if year < 1 or not 1 <= month <= 12:
                raise ValueError
            break
        except ValueError:
            print("Enter a valid month, for example 2026-11.")

    print(f"\n{calendar.month_name[month]} {year}")
    print("Mon Tue Wed Thu Fri Sat Sun")

    for week in calendar.monthcalendar(year, month):
        cells = []
        for day_number in week:
            if day_number == 0:
                cells.append("   ")
                continue

            chosen_day = date(year, month, day_number)
            if chosen_day > date.today():
                cells.append(f"{day_number:2} ")
                continue

            active = [
                record for record in data["habits"].values()
                if date.fromisoformat(record["created_on"]) <= chosen_day
            ]
            if not active:
                marker = " "
            else:
                all_done = all(
                    chosen_day.isoformat() in record["done_dates"] for record in active
                )
                marker = "*" if all_done else "-"
            cells.append(f"{day_number:2}{marker}")

        print(" ".join(cells))

    print("* = all habits that existed on that date were completed; - = not all were.")


# --------------------------- LEVEL 4: EXTRAS ------------------------------

def show_insights(data):
    """Show favourite completion weekdays and simple consistency comparisons."""
    if not data["habits"]:
        print("Add habits first to see insights.")
        return

    consistency = {}
    missed = {}
    print("\nHabit insights")

    for name, record in data["habits"].items():
        weekday_counts = Counter(
            date.fromisoformat(item).strftime("%A") for item in record["done_dates"]
        )

        if weekday_counts:
            highest = max(weekday_counts.values())
            best_days = [day for day, count in weekday_counts.items() if count == highest]
            weekday_text = ", ".join(best_days)
        else:
            weekday_text = "No completions yet"

        _, _, missed_30, rate_30 = period_stats(record, 30)
        consistency[name] = rate_30
        missed[name] = missed_30
        print(f"{name}: most-completed weekday(s): {weekday_text}")

    best_habit = max(consistency, key=consistency.get)
    missed_habit = max(missed, key=missed.get)
    print(f"\nMost consistent in the last 30 days: {best_habit} ({consistency[best_habit]:.1f}%)")
    print(f"Most missed days in the last 30 days: {missed_habit} ({missed[missed_habit]} days)")


def export_csv(data):
    """Export one row per habit to a CSV file that opens in spreadsheet apps."""
    if not data["habits"]:
        print("There are no habits to export.")
        return

    freeze = data["settings"]["streak_freeze_enabled"]
    try:
        with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "Habit", "Created On", "Weekly Target", "Completed Dates",
                "Current Streak", "Longest Streak", "7-Day Rate (%)",
                "30-Day Rate (%)", "Missed Days (Last 30 Days)"
            ])

            for name, record in data["habits"].items():
                current, longest = streak_values(record, freeze)
                _, _, missed30, rate30 = period_stats(record, 30)
                _, _, _, rate7 = period_stats(record, 7)
                writer.writerow([
                    name, record["created_on"], record["target_per_week"],
                    "; ".join(record["done_dates"]), current, longest,
                    round(rate7, 1), round(rate30, 1), missed30
                ])

        print(f"CSV report created: {CSV_FILE.name}")
    except OSError as error:
        print(f"Could not export the CSV report: {error}")


def settings_menu(data):
    """Turn the optional weekly streak freeze on or off."""
    current = data["settings"]["streak_freeze_enabled"]
    print(f"Streak freeze is currently {'ON' if current else 'OFF'}.")
    answer = input("Toggle this setting? (y/n): ").strip().lower()

    if answer == "y":
        data["settings"]["streak_freeze_enabled"] = not current
        if save_data(data):
            print(f"Streak freeze is now {'OFF' if current else 'ON'}.")
    else:
        print("Setting unchanged.")


def show_pending_habits(data):
    """At startup, list unfinished habits from highest streak to lowest."""
    if not data["habits"]:
        print("\nNo habits yet. Choose option 1 to add your first habit.")
        return

    today_text = date.today().isoformat()
    freeze = data["settings"]["streak_freeze_enabled"]
    pending = [
        (name, record) for name, record in data["habits"].items()
        if today_text not in record["done_dates"]
    ]
    pending.sort(key=lambda item: streak_values(item[1], freeze)[0], reverse=True)

    print("\nHabits still to complete today (highest streak first):")
    if not pending:
        print("All habits are completed today. Well done!")
        return

    for name, record in pending:
        current, _ = streak_values(record, freeze)
        print(f"- {name} ({current}-day streak)")


# ------------------------------ MAIN MENU ---------------------------------

def main():
    """Start the tracker and keep showing the menu until the user exits."""
    create_startup_backup()
    data = load_data()
    show_pending_habits(data)

    while True:
        print("\n========== HABIT TRACKER ==========")
        print("1. Add a habit")
        print("2. Rename a habit")
        print("3. Remove a habit")
        print("4. Mark a habit done")
        print("5. Show today's habits")
        print("6. Show full dashboard")
        print("7. Weekly summary")
        print("8. Monthly calendar")
        print("9. Habit insights")
        print("10. Export CSV report")
        print("11. Settings (streak freeze)")
        print("12. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_habit(data)
        elif choice == "2":
            rename_habit(data)
        elif choice == "3":
            remove_habit(data)
        elif choice == "4":
            mark_habit_done(data)
        elif choice == "5":
            show_habits(data)
        elif choice == "6":
            show_dashboard(data)
        elif choice == "7":
            show_weekly_summary(data)
        elif choice == "8":
            show_month_calendar(data)
        elif choice == "9":
            show_insights(data)
        elif choice == "10":
            export_csv(data)
        elif choice == "11":
            settings_menu(data)
        elif choice == "12":
            save_data(data)
            print("Goodbye. Your data has been saved.")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 12.")


if __name__ == "__main__":
    main()
