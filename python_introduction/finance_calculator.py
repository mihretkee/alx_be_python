monthly_income = float(input("enter your monthly income: "))
monthly_expenses = float(input("enter your total monthly expense: "))

monthly_savings = monthly_income - monthly_expenses
projected_savings =(monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print(f"Your monthly savings are ${monthly_savings:.0f}")
print(f"Projected savings after one year, with interest, is:${projected_savings:.0f}")

