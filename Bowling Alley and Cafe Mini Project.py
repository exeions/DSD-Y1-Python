cafe_food = {"Pizza": 7.0, "Chicken wings": 3.0, "Chips": 2.0, "Crisps": 1.0}
cafe_drink = {"Coca-Cola": 3.0, "Water": 2.0, "Latte": 2.0, "Tea": 2.0, "Fanta": 3.0, "Tango": 3.0, "J2O": 3.0}

VAT = 1.05
cost_per_hour = 20

bowling_lanes = [
    1,
    2,
    3,
    4
]

times = [9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

def booking_sys():
    global name
    global DOB

    name = input("Input your name for the booking: ")
    DOB = input("Input your data of birth for the booking [00/00/0000]: ")
    
    print(f"Here is a list of the available times [24 hour] {times}")
    start_time_of_booking = int(input("Input the start time of your booking [in hours]: "))
    end_time_of_booking = int(input("Input the end time of your booking [in hours]: "))

    diff = start_time_of_booking - end_time_of_booking
    if diff < 0:
        diff = diff * -1
        total_cost = (diff*cost_per_hour)*VAT
    else:
        total_cost = (diff*cost_per_hour)*VAT

    print("Here is a list of the available bowling lanes...")
    print(*bowling_lanes)
    global chosen_lane
    chosen_lane = int(input("Input your desired bowling lane for your booking: "))
    if chosen_lane in bowling_lanes:
        print("Successful!")
        bowling_lanes.remove(chosen_lane)
        print("Recording booking...")
        print("Booking recorded")
        return total_cost
    else:
        print(f"Lane '{chosen_lane}' not available or doesn't exist! Please try again...")
        booking_sys()

def foodOrder():
    while True:
        print(f"Please select a food item from the list: {cafe_food}")
        chosen_food = input("Input chosen food item here: ")

        if chosen_food in cafe_food:
            print("Ordered!")
            return cafe_food[chosen_food]
        else:
            print(f"Food item '{chosen_food}' doesn't exist. Please try again.\n")

def drinkOrder():
    while True:
        print(f"Please select a drink item from the list: {cafe_drink}")
        chosen_drink = input("Input chosen drink item here: ")

        if chosen_drink in cafe_drink:
            print("Ordered!")
            return cafe_drink[chosen_drink]
        else:
            print(f"Drink item '{chosen_drink}' doesn't exist. Please try again.\n")

def calculateCafeCosts():
    global total_costcafe
    total_costcafe = (foodOrder() + drinkOrder())*VAT
    print(f"The total cafe cost comes to £{round(total_costcafe, 2)}")

def calculateBookingCosts():
    global total_costbook
    total_costbook = booking_sys()
    print(f"The total cost of the booking comes to £{round(total_costbook, 2)}")

calculateBookingCosts()
calculateCafeCosts()

def calculateTotalCost():
    global total_cost_summary
    total_cost_summary = total_costcafe + total_costbook
    print(f"Your whole booking, including your other products bought. Come to a total of: £{round(total_cost_summary, 2)}")

def displaySummary():
    print("Your booking summary...")
    print(f"Booking Name: {name}\nDate Of Birth: {DOB}\nBowling Lane Selected: Lane {chosen_lane}\nTotal Booking/Product Cost: £{total_cost_summary}\n")

calculateTotalCost()
displaySummary()