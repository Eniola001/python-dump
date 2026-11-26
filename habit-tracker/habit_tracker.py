from datetime import date, timedelta

habits = {}


def add_habit():
    name = input("Enter habit name: ").strip()

    if not name:
        print("Habit name cannot be empty.")
        return

    if name in habits:
        print("This habit already exists.")
        return

    habits[name] = []

    print(f"'{name}' added successfully.")


def mark_habit_done():
    if not habits:
        print("You haven't added any habits yet.")
        return

    show_habits()

    try:
        habit_number = int(input("Habit number: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    habit_names = list(habits.keys())

    if habit_number < 1 or habit_number > len(habit_names):
        print("Invalid habit number.")
        return

    habit_name = habit_names[habit_number - 1]
    today = date.today().isoformat()

    if today in habits[habit_name]:
        print("This habit has already been completed today.")
        return

    habits[habit_name].append(today)

    print(f"'{habit_name}' marked as done!")


def calculate_streak(completed_dates):
    completed_dates = {
        date.fromisoformat(day) for day in completed_dates
    }

    today = date.today()

    if today in completed_dates:
        current_day = today
    else:
        current_day = today - timedelta(days=1)

    streak = 0

    while current_day in completed_dates:
        streak += 1
        current_day -= timedelta(days=1)

    return streak


def show_habits():
    today = date.today()
    today_string = today.isoformat()

    print(f"\nToday: {today.strftime('%a %d %b %Y')}\n")

    print(f"{'Habit':<25} {'Today':<10} {'Streak'}")
    print("-" * 45)

    for index, (name, completed_dates) in enumerate(habits.items(), start=1):
        status = "[x]" if today_string in completed_dates else "[ ]"
        streak = calculate_streak(completed_dates)

        print(f"{index}. {name:<22} {status:<10} {streak} days")


def main():
    while True:
        print("\n===== HABIT TRACKER =====")
        print("1. Add habit")
        print("2. Mark habit done")
        print("3. Show habits")
        print("4. Exit")

        choice = input("Menu choice: ").strip()

        if choice == "1":
            add_habit()

        elif choice == "2":
            mark_habit_done()

        elif choice == "3":
            show_habits()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


main()