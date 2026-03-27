name = input("Input name: ")
input(f"Hi {name}, welcome to the mala-bank, please proceed ")

user = input("Input username: ")
password = input("Input password: ")

if user == "hugo543" and password == "exeions":
    print(f"Welcome to your account {user}")

    add = input("Would you like to add to your account Y/N: ")
    balance = 0

    while add.upper() == "Y":
        add2 = float(input("Input amount adding: "))
        balance = balance + add2
        print(f"Your new balance is: {balance}")
        add = input("Would you like to add to your account Y/N: ")

    print(f"{name} your balance is: {balance}")
else:
    print("Incorrect user/pass!")