while True:
    task = input("Enter your task (or type 'exit' to quit): ")
    if task.lower() == "exit":
        print("Goodbye!")
        break

    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
