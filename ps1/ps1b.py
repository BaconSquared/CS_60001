current_savings = 0
rate = 0.04

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

portion_down_payment = (0.25)*total_cost
monthly_amount_saved = (annual_salary / 12) * portion_saved

num_months = 0
while current_savings < portion_down_payment:
    current_savings += current_savings*(rate)/12
    current_savings += monthly_amount_saved
    num_months += 1
    if num_months % 6 == 0:
        annual_salary += annual_salary*(semi_annual_raise)
        monthly_amount_saved = (annual_salary / 12) * portion_saved

print("Number of months: " + str(num_months))
