income = input("enter your monthly income: ")
expense = input("enter your total monthly expense: ")
monthly_saving = int(income) - int(expense)
print(monthly_saving)
saving =int(monthly_saving) * 12 + int((monthly_saving) * 12 * 0.05)
print(saving)
print(f"The user's monthly savings is ${monthly_saving}")
print(f"The user's annual saving is ${saving}")

