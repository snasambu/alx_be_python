# daily_reminder.py

def main():
    # Loop to get valid task input
    while True:
        task = input("Enter your task: ").strip()
        if task:
            break
        print("Task cannot be empty. Please enter a task.")

    # Loop to get valid priority
    while True:
        priority = input("Priority (high/medium/low): ").strip().lower()
        if priority in ("high", "medium", "low"):
            break
        print("Please enter a valid priority: high, medium, or low.")

    # Loop to get valid time-bound answer
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").strip().lower()
        if time_bound in ("yes", "no"):
            break
        print("Please answer 'yes' or 'no'.")

    print()  # Empty line for readability

    # Use match-case to handle different priority levels
    match priority:
        case "high":
            message = f"'{task}' is a high priority task"
        case "medium":
            message = f"'{task}' is a medium priority task"
        case "low":
            message = f"'{task}' is a low priority task"
        case _:
            message = f"'{task}' is a task"  # Fallback case, not expected to hit due to validation

    # Add time-bound detail if necessary
    if time_bound == "yes":
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it when you have free time."

    # Display final reminder
    print("Reminder:", message)

if __name__ == "__main__":
    main()
