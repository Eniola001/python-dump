# Habit Tracker — Complete Explanation and Presentation Transcript

This guide explains the final `habit_tracker_final.py` program. It is written so that you can use it both to understand the code and as a script when presenting the project.

## 1. Project introduction

**What to say during the presentation:**

> Our project is a command-line Habit Tracker written in Python. It allows a user to create habits, record the days on which they complete them, monitor their current and longest streaks, and review their progress.
>
> We developed the project in four levels. Level 1 introduces the basic tracking features. Level 2 adds habit management and input validation. Level 3 introduces file storage, summaries and completion statistics. Level 4 adds calendars, streak freezes, insights, backups and CSV reports.
>
> The program uses Python's standard library, so no external packages need to be installed.

The finished program is kept in one Python file to make it straightforward to run and demonstrate. The functions are grouped by the level or feature they support.

## 2. How the data is organised

The most important decision is how to store the habits.

The original Level 1 idea is a dictionary where each habit name points to a list of completed dates. For the later levels, we need to store extra information, such as when a habit was created and its weekly target. Therefore, the final version extends that idea: each habit name points to a small dictionary containing its information.

A simplified example is:

```python
{
    "settings": {
        "streak_freeze_enabled": False
    },
    "habits": {
        "Read 20 minutes": {
            "created_on": "2026-11-20",
            "target_per_week": 5,
            "done_dates": [
                "2026-11-21",
                "2026-11-22",
                "2026-11-23"
            ]
        },
        "Exercise": {
            "created_on": "2026-11-22",
            "target_per_week": 4,
            "done_dates": []
        }
    }
}
```

**What to say during the presentation:**

> The main data is stored in a dictionary called `data`. Inside it, the `habits` dictionary contains every habit. Each habit has a creation date, a weekly target and a list of completion dates.
>
> Dates are saved as text in the `YYYY-MM-DD` format. This makes them easy to store in JSON and compare after converting them into Python date objects.
>
> There is also a `settings` section. It stores whether streak freeze is switched on or off.

This structure is useful because the program can add more information to a habit without creating separate dictionaries for every feature.

## 3. The Python modules used

At the top of the program, we import tools from Python's standard library:

| Module or class | What it does |
|---|---|
| `date`, `timedelta` | Gets today's date and moves forwards or backwards by a number of days. |
| `datetime` | Creates timestamps for backup filenames. |
| `Path` | Builds file and folder paths. |
| `json` | Saves and loads the tracker data. |
| `calendar` | Generates the layout of a chosen month. |
| `csv` | Writes the report in spreadsheet-friendly format. |
| `shutil` | Copies the data file to create a backup. |
| `Counter` | Counts how often each weekday appears in a habit's completion history. |

No third-party library is required.

The program also sets its file paths relative to the location of the Python script. This means `habits.json`, the `backups` folder and the CSV report are stored beside the script, rather than depending on whichever folder the terminal happens to be using.

---

# Level 1 — Basic Habit Tracking

## 4. What Level 1 required

Level 1 required the program to:

1. Store habits and their completion dates.
2. Add a habit.
3. Mark a habit as completed today.
4. Display every habit's status for today.
5. Calculate the current consecutive-day streak.

**What to say during the presentation:**

> Level 1 focuses on the main purpose of the application: tracking whether a habit has been completed and calculating how consistently the user has completed it.
>
> We use a dictionary to organise the habits and a list to store the dates on which each habit was completed. We use functions so that adding a habit, marking it complete, calculating its streak and displaying the results are handled separately.

## 5. Adding a habit

The `add_habit(data)` function asks the user for a habit name and a weekly target. It checks that the name is not empty and that another habit does not already have the same name. It then creates a new record:

```python
data["habits"][name] = {
     "created_on": date.today().isoformat(),
     "target_per_week": target,
     "done_dates": []
 }
```

The `created_on` value records the date the habit was created. The `done_dates` list starts empty because the user has not recorded any completions yet.

The weekly target is included in the final version because it is needed by Level 3. The `ask_target()` function keeps asking until the user enters a whole number from 1 to 7.

## 6. Marking a habit as done

The `mark_habit_done(data)` function first calls `choose_habit(data)`. That function displays the habits with numbers and lets the user select one. Entering `0` cancels the action.

The function then asks for a completion date. Pressing Enter selects today. This also supports the Level 2 requirement to record a past completion.

Before adding the date, the program checks that:

- The date follows the required `YYYY-MM-DD` format.
- The date is not in the future.
- The date is not earlier than the habit's creation date.
- The same habit has not already been completed on that date.

If all checks pass, the date is appended to `done_dates` and the list is sorted.

## 7. Calculating a current streak

The `streak_values(record, freeze_enabled)` function returns two numbers: the current streak and the longest streak.

With streak freeze switched off, the basic streak logic works as follows:

1. If the habit was completed today, begin checking from today.
2. Otherwise, begin checking from yesterday. An unfinished current day should not immediately break a streak.
3. Move backwards through the dates, counting consecutive completions.
4. Stop the current streak when a missed day is encountered.

The same function scans the habit's history to find the longest streak. The function is extended in Level 4 to account for an optional freeze day.

For example, if the habit was completed on Monday, Tuesday and Wednesday, the streak is three days. If Thursday is missed and no freeze is available, the ongoing streak is broken.

## 8. Displaying today's status

The `show_habits(data)` function loops through the habits and checks whether today's date appears in each habit's `done_dates` list.

It displays `[x]` when today's date is present and `[ ]` when it is absent. It also calls `streak_values()` to display the current streak.

**What to say during the presentation:**

> The display function does not need to calculate the streak itself. It asks the streak function for the result and then prints it. This separation keeps the calculation logic in one place and makes it reusable in the dashboard and reports.

---

# Level 2 — Habit Management and Validation

## 9. What Level 2 required

Level 2 adds the ability to:

1. Rename a habit.
2. Remove a habit.
3. Reject empty and duplicate habit names.
4. Prevent a habit from being marked twice on the same date.
5. Record a completion for a past date.
6. Reject invalid dates and future dates.
7. Calculate a completion rate for the last seven days.

**What to say during the presentation:**

> Level 2 makes the tracker more practical. Users can manage their habits after creating them, and the program checks their input instead of accepting invalid information or crashing.

## 10. Renaming and removing habits

The `rename_habit(data)` function asks the user to select an existing habit and enter a new name. It checks that the new name is not blank and is not already being used by another habit.

To rename a dictionary key without losing its information, the function builds a new dictionary. It puts the old habit's record under the new name. The creation date, target and completion history are therefore preserved.

The `remove_habit(data)` function also asks the user to select a habit. Before deleting it, the program asks for confirmation. The habit is deleted only when the user answers `y`.

## 11. Rejecting duplicate and empty names

The program uses `.strip()` to remove spaces from the beginning and end of the name. If nothing remains, the name is empty and the user is asked again.

It uses `.casefold()` when comparing names. This makes duplicate checking case-insensitive. For example, `Exercise` and `exercise` are treated as the same name.

## 12. Validating completion dates

The `parse_date(value)` function attempts to convert a date string into a Python date object. It returns `None` when the input is invalid or does not use the exact `YYYY-MM-DD` format.

The `ask_completion_date(record)` function then checks whether the selected date is in the future or earlier than the habit's creation date. It repeats the question until the user enters a valid date.

**What to say during the presentation:**

> These checks protect the completion history. A user cannot record a future completion, record a completion before the habit existed, or enter the same completion twice for one day.

## 13. Seven-day completion rate

The `period_stats(record, number_of_days)` function is reusable. It can calculate statistics for any number of days, including 7 and 30.

For a seven-day rate, it:

1. Finds the first date in the seven-day period.
2. Moves that date forward if the habit was created more recently.
3. Counts the active calendar days in the period.
4. Counts how many of those dates appear in the completion history.
5. Divides completed days by active days and multiplies by 100.

The formula is:

```text
Completion rate = (Completed days / Active days) x 100
```

For example, five completed days out of seven active days gives a completion rate of approximately 71.4%.

---

# Level 3 — Saving Data and Progress Summaries

## 14. What Level 3 required

Level 3 adds:

1. JSON saving and loading.
2. Handling missing, empty or corrupted data files.
3. Current and longest streaks.
4. A Monday-to-Sunday weekly summary.
5. A weekly target for each habit.
6. A 30-day completion percentage.

**What to say during the presentation:**

> Level 3 makes the tracker persistent. In the earlier level, the data existed only while the program was running. Now the program saves the data to a JSON file and loads it again the next time it starts.
>
> This level also expands the dashboard to show more useful statistics, including the longest streak, weekly progress and the 30-day completion rate.

## 15. Saving and loading JSON

The file is called `habits.json` and is stored beside the Python script.

The `save_data(data)` function converts the dictionary into JSON text and writes it to the file. It first writes to a temporary file and then replaces the main file. This reduces the chance of leaving a partly written main file if saving is interrupted.

The `load_data()` function runs when the program starts. It checks whether the file exists, whether it is empty and whether its contents are valid JSON with the expected structure.

If the file is missing, empty or damaged, the program displays a message and starts with an empty tracker instead of immediately crashing. The original file is not changed by the loading function. A backup is attempted before loading, when an existing file is available.

The program also checks saved habit records and ignores invalid date entries or invalid weekly targets. An invalid target is replaced with the default of five days per week.

## 16. Current and longest streaks

The `streak_values()` function returns both values:

- **Current streak:** the consecutive run that reaches today, or yesterday when today has not been completed.
- **Longest streak:** the largest consecutive run found in the habit's recorded history.

These values are displayed in the dashboard and included in the CSV report.

## 17. Weekly summary grid

The `current_week_dates()` function calculates the dates from the current Monday to Sunday.

The `show_weekly_summary(data)` function compares each date with the habit's completion list:

- `x` means completed.
- `-` means missed.
- A blank cell means that the date is still in the future.

Future days are left blank because they have not been missed; they have not happened yet.

The function also counts the completed days so far this week and compares that number with the habit's weekly target.

## 18. Weekly target and 30-day rate

Each habit has a `target_per_week` value from 1 to 7. The dashboard counts the habit's completions from Monday up to the current day and reports whether the target has been reached.

The 30-day completion percentage uses the same calculation as the seven-day percentage, but looks at a 30-day period. For a habit created less than 30 days ago, only the days since its creation are included.

**What to say during the presentation:**

> The dashboard brings the statistics together. It shows whether each habit was completed today, the current and longest streaks, the seven-day and 30-day completion rates, and progress towards the weekly target.

---

# Level 4 — Advanced Features and Reporting

## 19. What Level 4 required

Level 4 adds:

1. A text calendar for a selected month.
2. An optional weekly streak freeze.
3. Insights about completion weekdays and consistency.
4. CSV report export.
5. Automatic backups at startup.
6. A startup list of unfinished habits, sorted by current streak.

**What to say during the presentation:**

> Level 4 adds features that make the tracker more useful for reviewing behaviour over time. It can show a monthly calendar, protect a streak with an optional freeze day, identify completion patterns and export a report that can be opened in spreadsheet software.

## 20. Monthly text calendar

The `show_month_calendar(data)` function asks for a month in `YYYY-MM` format. It uses Python's `calendar` module to create the month layout and prints the result as text.

For each date, the program checks which habits had already been created by that date. If all those active habits were completed, it prints `*`. Otherwise, it prints `-`.

Future dates are left unmarked. Dates before any habit was created are also left unmarked because there were no active habits to complete.

## 21. Streak freeze

The streak freeze can be switched on or off from the settings menu. Its setting is saved in the JSON file, so it remains the same after restarting the program.

When it is enabled, one missed day in each Monday-to-Sunday week can be protected for a habit, provided that the habit already has an active streak. The protected day counts as part of the streak. A second missed day in that same week will break the streak if it is not completed.

The rule is applied separately to each habit. It is optional, so the normal streak calculation is used when the setting is off.

## 22. Habit insights

The `show_insights(data)` function uses each habit's completion history to show:

- The weekday or weekdays on which the habit has been completed most often.
- The most consistent habit, measured by the 30-day completion percentage.
- The habit with the most missed days in the last 30 days.

The `Counter` class counts how many recorded completions occurred on each weekday. If two weekdays have the same highest count, both are displayed.

The 30-day period is used for the consistency and missed-day comparison so habits can be compared over the same recent time window.

## 23. CSV report

The `export_csv(data)` function creates `habit_report.csv` beside the Python script.

The report contains one row per habit. It includes the habit name, creation date, weekly target, completion dates, current streak, longest streak, seven-day rate, 30-day rate and missed days in the last 30 days.

CSV is useful because it can be opened in Microsoft Excel, Google Sheets and other spreadsheet programs.

## 24. Automatic backups and unfinished habits

The `create_startup_backup()` function runs before the program loads the JSON file. If `habits.json` already exists, it copies the file into a `backups` folder. The backup filename includes a timestamp so that earlier backups are not overwritten.

The `show_pending_habits(data)` function runs after the data has loaded. It finds habits that have not been completed today and sorts them by current streak, highest first. This gives the user a reminder of what remains to be done.

**What to say during the presentation:**

> The backup feature helps preserve an earlier copy of the saved data. The pending-habits feature also makes the tracker useful as soon as it opens, because it immediately shows which habits remain incomplete today.

---

# 25. How the main program works

The `main()` function connects all the other functions.

When the program starts, it:

1. Creates a backup if a previous JSON file exists.
2. Loads the saved data.
3. Displays habits that are still incomplete today.
4. Shows the menu inside a `while` loop.

The user selects a menu number. An `if`/`elif` structure calls the function for that option. The loop continues until the user selects Exit. Before exiting, the program saves the data.

The final lines are:

```python
if __name__ == "__main__":
    main()
```

This means the menu starts when the file is run directly. It also allows the functions to be imported for testing without automatically starting the menu.

## 26. How to run the project

1. Install Python 3 if it is not already installed.
2. Keep `habit_tracker_final.py` in a folder where you can create files.
3. Open a terminal in that folder.
4. Run:

```bash
python habit_tracker_final.py
```

If your computer uses the `python3` command, run:

```bash
python3 habit_tracker_final.py
```

The program creates these files and folders as needed:

```text
Habit Tracker/
    habit_tracker_final.py
    habits.json             # saved habits
    habit_report.csv        # created when CSV export is selected
    backups/                # timestamped JSON backups
```

## 27. Recommended live demonstration

For a short presentation, use this sequence:

1. Start the program and explain that it loads saved information and lists unfinished habits.
2. Add `Read 20 minutes` with a weekly target of 5.
3. Add `Drink water` with a weekly target of 7.
4. Add `Exercise` with a weekly target of 4.
5. Display today's habits and explain the `[ ]` status.
6. Mark one habit done for today and show the `[x]` status.
7. Try to mark it done again to demonstrate duplicate prevention.
8. Open the dashboard and explain the streaks, completion percentages and weekly target.
9. Open the weekly summary and explain the `x`, `-` and blank symbols.
10. Open the monthly calendar and insights.
11. Toggle streak freeze and explain the rule.
12. Export the CSV report.
13. Exit and restart the program to demonstrate that the habits are still saved and that a startup backup is created.

For a reliable presentation, add and complete a few habits before the presentation day. This gives the dashboard, weekly summary, calendar and insights meaningful history to display.

## 28. Important behaviour and assumptions

These rules explain how the program interprets the requirements:

- A habit's weekly target is compared with the number of completions recorded from Monday through today. The target is not prorated when a habit is created partway through a week.
- Completion percentages count calendar days in the selected period, starting no earlier than the habit's creation date. Today is included in the denominator.
- The current streak does not treat an unfinished today as a missed day. It checks through yesterday instead.
- A streak freeze protects at most one missed day per Monday-to-Sunday week, per habit, and only when a streak is already active.
- The “most consistent” insight means the highest 30-day completion percentage. The “most missed” insight means the highest number of missed days during the last 30 days.
- The monthly calendar's `*` means every habit that existed on that date was completed. A habit created later is not counted for earlier dates.
- The first program run cannot create a backup if there is no previous `habits.json` file.

This is a defensive beginner project, not a guarantee against every possible computer or storage failure. It validates normal user input and handles common file problems, but important data should still be backed up separately.

## 29. Closing statement for the presentation

> In conclusion, the Habit Tracker demonstrates several core Python concepts in one practical application. These include dictionaries, lists, functions, loops, conditional statements, date calculations, input validation, file handling, JSON, CSV and standard-library modules.
>
> The project was developed in stages so that each level builds on the previous one. It begins with basic habit tracking and progresses to persistent storage, reporting, streak management and insights. The final result gives users a simple way to record habits and review their consistency over time.
