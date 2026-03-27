name = input("Input patient name: ")
age = int(input("Input patient age: "))
bill = float(input("Input bill amount (gbp): "))

discount = False
discountValue = 0.95
VAT = 1.1

totalBill = VAT*bill

if age < 18:
    discount = True
else:
    discount = False

if discount == True:
    totalBill = totalBill*discountValue

print(f"Patient: {name}, Age: {age}, Bill: {round(totalBill, 2)} pounds")

if totalBill > 1000:
    paymentPlan = input("Would you like to pay in months/years/N/A: ").lower()

    if paymentPlan == "months":
        time = int(input("How many months would you like to pay for: "))
        monthPay = totalBill/time

        print(f"Converted to months, your total bill for this month comes to {round(monthPay, 2)} ppunds which will take you {time} months")
    elif paymentPlan == "years":
         time = int(input("How many years would you like to pay for: "))
         yearPay = totalBill/time

         print(f"Converted to years, your total bill for this year comes to {round(yearPay, 2)} pounds which will take you {time} years")
    else:
       print(f"Your total bill comes to {totalBill} pounds") 