import math, random, datetime, numpy

# number = float(input("Input a number: "))
# sqrt = math.sqrt(number)
# squared = number * number
# rounded = round(number)

# radius = rounded
# pi = 3.141

# area = pi*(radius*radius)
# print(f"Area of the circle is: {round(area, 2)}")

# print(round(sqrt, 2), round(squared, 2), round(rounded, 2))

# lives = 0
# wins = 0
# rounds = 1

# while lives < 3:
    
#     start = input("Press Enter To Start! ")

#     rounds +=1

#     random_dice = random.randint(1,6)
#     random_dice_2 = random.randint(1,6)

#     total_score = random_dice + random_dice_2

#     if total_score == 7 or total_score == 11:
#         print(total_score)
#         print("You Win!")
#         wins +=1
#     else:
        
#         print(total_score)
        
#         print("Try Again.")
#         lives +=1

#         random_dice = random.randint(1,6)
#         random_dice_2 = random.randint(1,6)

#         total_score = random_dice + random_dice_2

        
#     win_percentage = (wins / rounds) * 100
#     print(f"Win percentage: {round(win_percentage, 2)}%")

import datetime

today = datetime.date.today()
now = datetime.datetime.now()

print("Today's date:", today.strftime("%d/%m/%Y"))
print("Current time:", now.strftime("%H:%M:%S"))

year = int(input("Enter birth year (YYYY): "))
month = int(input("Enter birth month (MM): "))
day = int(input("Enter birth day (DD): "))

birth = datetime.date(year, month, day)

age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
print("Age:", age)

next_birthday = birth.replace(year=today.year)
if next_birthday < today:
    next_birthday = next_birthday.replace(year=today.year + 1)

print("Days until next birthday:", (next_birthday - today).days)