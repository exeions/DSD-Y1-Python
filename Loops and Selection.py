def passwordChecker():
    passw = input("Input password: ")
    password = "malachi"

    while True:
        if passw == password:
            print("Logged in.")
            break
        else:
            print("Incorrect password, try again.. ")
            passw = input("Input password: ")

def patientMenuSystem():
    name = input("Input patient name: ")
    age = int(input("Input patient age: "))
    height= float(input("Height (meters): "))
    weight= float(input("Weight (kg): "))
    
    bmi = weight/(height**2)
    
    if bmi > 30:
        print("obese.")
    elif bmi > 25:
        print("overweight.")
    elif bmi < 25:
        print("healthy weight.")
    elif bmi < 18:
        print("under-weight.")
    
    