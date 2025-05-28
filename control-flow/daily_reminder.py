task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
reminder = ""
match priority:
    case "high":
        reminder = f"reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"reminder: '{task}' is a low priority task"
    case _:
        reminder = f"reminder: '{task}' is an unknown priority level"
if time_bound == "yes":
        reminder += " that requires immediate attention today!"
else:
        reminder += " consider completing it when you have free time."
print(reminder)

    

       
