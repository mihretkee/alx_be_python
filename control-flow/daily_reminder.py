task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
Reminder = ""
match priority:
    case "high":
        Reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        Reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        Reminder = f"Reminder: '{task}' is a low priority task"
    case _:
        Reminder = f"Reminder: '{task}' is an unknown priority level"
if time_bound == "yes":
        Reminder += " that requires immediate attention today!"
else:
        Reminder += " consider completing it when you have free time."
print("Reminder:")

    

       
