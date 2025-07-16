print("Type 'exit' to quit at any time.")

while True:
    task = input("Enter your task: ")
    if task.lower() == "exit":
        print("Goodbye!")
        break

    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    match priority:
        case "high":
            reminder = f"Reminder: '{task}' is a high priority task"
        case "medium":
            reminder = f"Reminder: '{task}' is a medium priority task"
        case "low":
            reminder = f"Reminder: '{task}' is a low priority task"
        case _:
            reminder = f"Reminder: '{task}' has an unknown priority"

    if time_bound == "yes":
        reminder += " that requires immediate attention today!"

    print("\n" + reminder + "\n")
