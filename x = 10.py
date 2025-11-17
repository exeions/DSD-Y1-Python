# num = int(input("Input number 1-100: "))

# if num >= 1 and num <= 100:
#     print(num)
# else:
#     print("num has to be between 1-10")

from tkinter import *
from tkinter import ttk

win= Tk()

win.geometry("300x300")

label1 = Label(text="Age").pack()

button = Button(text="Start").pack()

entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()

def pressed():
    num = entry.get()
    if num >= 1 and num <= 100:
        print(num)
        label.configure(text=num)
    else:
        print("num has to be between 1-10")
        label.configure(text=num)

label = Label(text="nul").pack()

win.mainloop()