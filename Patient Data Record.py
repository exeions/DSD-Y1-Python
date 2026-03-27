import tkinter as tk

def patientRecordSystem():
    name = input("Input name: ")
    age = int(input("Input age: "))
    height = float(input("Input height (cm/m): "))
    weight = float(input("Input weight (kg): "))

    DOB = input("Input dateOfBirth (**/**/****): ")

    print(f"name: {name}, age: {age}, height: {height}cm/m, weight: {weight}kg, dateOfBirth: {DOB}")

def BMI():
    weight = float(input("Input weight (kg): "))
    height = float(input("Input height (meters): "))
    
    cBMI = weight/(height**2)
    cat = ""
    if cBMI < 18.5:
        cat = "underweight"
    elif cBMI < 24.9:
        cat = "normal"
    elif cBMI < 29.9:
        cat = "overweight"
    elif cBMI < 34.9:
        cat = "class 1 obesity"
    elif cBMI < 39.9:
        cat = "class 2 obesity"
    elif cBMI < 50:
        cat = "class 3 obesity"
    elif cBMI > 50:
        cat = "class 4 obesity"
    print(f"Your BMI is: {cBMI} and you're in the {cat} category")

def dosage():
    max = 4000 ## Paracetamol (mg)
    total = 0
    while max > 0:
        print(f"Your maximum dose is {max}mg of paracetamol")
        dose = float(input("Input (MG) of paracetamol: "))
        max = max - dose
        
        total = total + dose

        print(f"You have taken {dose}mg of paracetamol and your max is now {max}..")
        if max > 0:
            end = input("Would you like to take more paracetamol? Y/N  ")
            if end.lower() == "y":
                print("ok, proceeding..")
            else:
                break
        
    print(f"You have taken {total}mg of paracetamol")

def billing():
    room_costs = 60 ## Per day
    treatment = float(input("Input treatment costs: "))
    doctor = float(input("Input doctor costs: "))
    days_stayed = int(input("Input days stayed: "))

    totalService = treatment+doctor+(days_stayed*room_costs)
    VAT = 0.03 # 3% VAT FEE
    total = totalService*(1+VAT)
    tVAT = total*VAT

    print(f"Your total cost is £{total} with a VAT of £{tVAT}")


window = tk.Tk()
window.geometry("256x256")

title = tk.Label(text="Patient Record Sys")
title.pack()

button = tk.Button(window, text="PatientRecordSystem", width=25, command=patientRecordSystem)
button.pack()

window.mainloop()