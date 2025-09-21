# daily_reminder.py
# Requires Python 3.10+ for match / case

task = input("Enter your task:").strip()
priority = input("Priority (high/medium/low):").strip().lower()
time_bound = input("Is it time-bound? (yes/no):").strip().lower()

match priority:
    case "high":
        priority_text = "high priority task"
    case "medium":
        priority_text = "medium priority task"
    case "low":
        priority_text = "low priority task"
    case _:
        print("Invalid priority. Please enter high, medium, or low.")
        raise SystemExit(1)

if time_bound == "yes":
    print(f"Reminder: '{task}' is a {priority_text} that requires immediate attention today!")
elif time_bound == "no":
    print(f"Note: '{task}' is a {priority_text}. Consider completing it when you have free time.")
else:
    print("Invalid response for time-bound. Please answer yes or no.")
