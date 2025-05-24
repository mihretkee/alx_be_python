monthly_income = float(input("enter your monthly income: "))
monthly_expenses = float(input("enter your total monthly expense: "))
monthly_savings = int(monthly_income) - int(monthly_expenses)
print(monthly_savings)
projected_savings =int(monthly_savings) * 12 + int((monthly_savings) * 12 * 0.05)
print(saving)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one year, with interest, is:${projected_savings}")

