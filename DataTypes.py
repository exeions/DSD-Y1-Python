# x = 25
# y = 3.14

# print(type(x), type)

# a = 10
# b = 3

# print(a/b)
# print(a//b)
# print(a * 2.5)

from tkinter import *
from tkinter import simpledialog

root = Tk()
root.withdraw()

scrollbar =  Scrollbar(root)
User_input = simpledialog.askstring(title="Test Average Calculator", prompt="Input Score1: ")
User_input2 = simpledialog.askstring(title="Test Average Calculator", prompt="Input Score2: ")
User_input3 = simpledialog.askstring(title="Test Average Calculator", prompt="Input Score3: ")

avg = (int(User_input)+int(User_input2)+int(User_input3))/3
print(avg)
# Score1 = int(input("Input first test score. "))
# Score2 = int(input("Input second test score. "))
# Score3 = int(input("Input third test score. "))

# avg = (Score1+Score2+Score3)/3
# print(avg)
