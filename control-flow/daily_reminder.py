print("Type 'exit' to quit at any time.")

while True:
    task = input("Enter your task: ")
    if task.lower() == "exit":
        print("Goodbye!")
        break

    priority = input("Priority (high/medium/low): ")
    time_bound = input("Is it time-bound? (yes/no): ")

    reminder = f"Reminder: '{task}' is a {priority} priority task"
    if time_bound.lower() == "yes":
        reminder += " that requires immediate attention today!"
    else:
        reminder += "."

    print("\n" + reminder + "\n")
