while True:
    task = input("Enter your task: ").strip()
    if task:
        break

while True:
    priority = input("Priority (high/medium/low): ").lower().strip()
    if priority in ("high", "medium", "low"):
        break

while True:
    time_bound = input("Is it time-bound? (yes/no): ").lower().strip()
    if time_bound in ("yes", "no"):
        break

match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."
    else:
        reminder += " that can be handled later."

print()  # NEWLINE BEFORE PRINTING REMINDER
print(reminder)
