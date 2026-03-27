days_hired = int(input("How many days to hire car: "))
start_mileage = int(input("Input the start mileage: "))
end_mileage = int(input("Input the end mileage: "))

day_price = 20
mile_price = 0.05

miles_driven = end_mileage - start_mileage

total_day = day_price * days_hired
total_mile = mile_price * miles_driven

total = total_day + total_mile

print(f"The total price for days driven is £{total_day} and the total price for miles driven is £{total_mile}. This comes to a total of £{total}")