def fitnessTracker():
    def calorieBurn():
        CPM = int(input("Input your calories per minute: "))
        workoutTime = float(input("Input workout time (minutes): "))

        caloriesBurnt = CPM * workoutTime
        print(f"Your calories burnt in {workoutTime} minutes is {caloriesBurnt}kcal")

    def stepConversion():
        steps = int(input("Input your total steps: "))
        distance = round(steps/1300, 3)

        print(f"Estimated to be {distance}km")

    def medicationTiming():
        totalMinutes = float(input("Input total minutes until next medication: "))
        hours = totalMinutes // 60
        minutes = totalMinutes % 60

        print(f"You should take your medication in {hours} hours and {minutes} minutes")

    def medicinePackUsage():
        packet = 10

        takenTablets = int(input("How many tablets have you taken: "))
        left = round(takenTablets % 10)
        less = round(10 - takenTablets)

        if takenTablets > 10:
            print(f"You have {left} tablets left to take, please get another packet.")
        else:
            print(f"You have {less} tablets to make a full packet.")
        

    option = int(input("Options [TYPE NUMBER FOR OPTION]: 1.Calorie burn, 2.Step conversion, 3.Medication timing, 4.Medicine pack usage, 5.Heat recovery "))
    
    if option == 1:
        calorieBurn()
    if option == 2:
        stepConversion()
    if option == 3:
        medicationTiming()
    if option == 4:
        medicinePackUsage()



def healthCareCalculator():
    name = input("Input your patient name: ")
    age = int(input("Input your patient age: "))
    cost = round(float(input("Input cost of your treatment: ")), 2)

    VAT = 1.005
    free = False
    package = False

    ## Calc 1
    if age < 18:
        print("You qualify for free healthcare as you're under the age of 18!")
        free = True
    elif age >= 18 and age < 60:
        print("You do not qualify for free healthcare or any benefits as you are an adult.")
    elif age >= 60:
        print("You get the pensioner package!")
        package = True
    totalCost = round(cost * VAT, 2)

    if free == True:
         totalCost = 0
         print(f"Your total cost comes to {totalCost} gbp")
    if package == True:
        totalCost = round(totalCost * 0.8, 2)
        print(f"Your total cost comes to {totalCost} gbp")
    if free == False and package == False:
        print(f"Your total cost comes to {totalCost} gbp")

healthCareCalculator()

##well organised
##not breakable
##takes inputs and accuratly send outputs