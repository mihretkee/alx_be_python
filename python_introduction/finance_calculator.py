monthly_income = input("enter your monthly income: ")
monthly_expenses = input("enter your total monthly expense: ")
monthly_savings = int(monthly_income) - int(monthly_expenses)
print(monthly_savings)
saving =int(monthly_savings) * 12 + int((monthly_savings) * 12 * 0.05)
print(saving)
print(f"The user's monthly savings is ${monthly_savings}")
print(f"The user's annual saving is ${saving}")

