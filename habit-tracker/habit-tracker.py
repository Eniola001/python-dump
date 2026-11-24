data = {
    "settings": {
        "streak_freeze_enabled": False
    },
    "habits": {
        "Read 20 minutes": {
            "created_on": "2026-11-19",
            "target_per_week": 5,
            "done_dates": [
                "2026-11-19",
                "2026-11-20",
                "2026-11-21",
                "2026-11-23"
            ]
        },
        "Drink water": {
            "created_on": "2026-11-20",
            "target_per_week": 7,
            "done_dates": [
                "2026-11-20",
                "2026-11-21"
            ]
        }
    }
}

def add_habit(data, habit_name, target_per_week):
    habit_name = habit_name.strip()
    target_per_week = int(target_per_week)

    ldata["habits"]["Exercise"] = {
        "created_on": "2026-11-21",
        "target_per_week": 4,
        "done_dates": []
    }
    
