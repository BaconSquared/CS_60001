#total_cost = 2000000
#portion_down_payment = 500000
current_savings = 0
rate = 0.04
#annual_salary = 85000
#portion_saved = .08

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

portion_down_payment = (0.25)*total_cost
monthly_amount_saved = (annual_salary / 12) * portion_saved
print(monthly_amount_saved)
print(portion_down_payment)

num_months = 0
while current_savings < portion_down_payment:
    current_savings = current_savings + current_savings*(rate)/12
    current_savings += monthly_amount_saved
    #print(current_savings)
    num_months += 1

print("Number of months: " + str(num_months))
