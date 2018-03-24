current_savings = 0
rate = 0.04
semi_annual_raise = .07
total_cost = 1000000
portion_down_payment = (0.25)*total_cost
num_months = 36

initial_salary = int(input("Enter the starting salary: "))

found = False
num_guesses = 0
epsilon = 100
low = 0
high = 10000
portion_saved = int((high + low) / 2)

while abs(low - high) > 1:
    num_guesses += 1
    current_savings = 0
    salary = initial_salary
    monthly_amount_saved = (portion_saved / 10000) * (initial_salary / 12)

    for month in range(1, num_months + 1):
        current_savings += current_savings*(rate)/12
        current_savings += monthly_amount_saved

        if abs(current_savings - portion_down_payment) <= 100:
            low = high
            found = True
            break
        if current_savings > portion_down_payment + 100:
            break

        if month % 6 == 0:
            salary += salary * (semi_annual_raise)
            monthly_amount_saved = (salary / 12) * (portion_saved / 10000)

    if current_savings < portion_down_payment - 100:
        low = portion_saved
    else:
        high = portion_saved

    portion_saved = int((high + low) / 2)

if found == False:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate: " + str(portion_saved / 10000))
    print("Steps in bisection search: " + str(num_guesses))
