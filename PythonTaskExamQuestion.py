day_hire = 20
mile_driven = 0.05

car_hired = int(input("Input number of days car was hired for (must be atleast 1): "))
start_mileage = int(input("Input the start mileage of the hire period: "))
end_mileage = int(input("Input the end mileage of the hire period: "))

miles_driven = end_mileage - start_mileage

day_hire_total = day_hire * car_hired
mile_driven_total = mile_driven * mile_driven

total_charge = day_hire_total + mile_driven_total

print(f"The total charge comes to £{round(total_charge, 2)}.")