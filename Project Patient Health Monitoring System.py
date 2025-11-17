def conversionSys():
    gConversion = 18.018 ## Constant conversion value for glucose
    cConversion = 38.67 ## Constant conversion value for cholesterol

    test_type = input("Input test type glucose/cholesterol: ")

    if test_type.lower() == "glucose":
        test_value = float(input("Input value: "))
        unit = input("Input unit (mg/dL) (mmol/L) ").lower()

        if unit == "mmol/l" or unit == "mmoll":
            test_value = test_value*gConversion ## Converts from mmol/L to mg/dL
            print(f"Your value is {test_value} mg/dL")

        elif unit == "mg/dl" or unit == "mgdl":
            test_value = test_value/gConversion ## Converts from mg/dL to mmol/L
            print(f"Your value is {test_value} mmol/L")
        else:
            print("You may have got the unit wrong. It only accepts mg/dL or mmol/L!")
    elif test_type.lower() == "cholesterol":
        test_value = float(input("Input value: "))
        unit = input("Input unit (mg/dL) (mmol/L) ").lower()

        if unit == "mmol/l" or unit == "mmoll":
            test_value = test_value*cConversion ## Converts from mmol/L to mg/dL
            print(f"Your value is {test_value} mg/dL")

        elif unit == "mg/dl" or unit == "mgdl":
            test_value = test_value/cConversion ## Converts from mg/dL to mmol/L
            print(f"Your value is {test_value} mmol/L")
        else:
            print("You may have got the unit wrong. It only accepts mg/dL or mmol/L!")
    else:
        print("Invalid type!")

def averageTemperatureTracker():
    threshold = 38 ## Constant threshold
    
    i = 0
    tempTotal = 0

    while i < 3:
        add = float(input("Input temperature reading: "))
        tempTotal = tempTotal + add
        i = i + 1

    
    avg = tempTotal/3
    print(f"The average temperature reading is {round(avg, 2)}")
    if avg > threshold:
        print("You have exceeded the fever threshold! Be careful.")

def heartRateMonitor():

    max_heart_rate_base = 220 ## Constant for the max heart rate base.
    classH = "" ## Class

    age = int(input("Input your age: "))
    resting_heart_rate = float(input("Input your resting heart rate: "))

    safe_maximum = max_heart_rate_base - age
    if resting_heart_rate < 60:
        classH = "low"
    elif resting_heart_rate < 100:
        classH = "normal"
    elif resting_heart_rate > 100:
        classH = "high"
    print(f"Your safe maximum heart rate would be {safe_maximum} bpm (beats per minute) and your resting heart rate is {classH}")
    
def patientHydrationTracker():
    daily_goal = 3.7 ## Constant daily goal.
    
    water_intake = float(input("Input todays water intake (L/litres) "))
    
    if water_intake < daily_goal:
       print(f"You are NOT meeting the goal with an intake of {water_intake}L which is {round(daily_goal - water_intake, 2)}L off the goal")
    elif water_intake > daily_goal:
         print(f"You are meeting the goal with an intake of {water_intake}L which is {round(water_intake - daily_goal, 2)}L more than the goal")
