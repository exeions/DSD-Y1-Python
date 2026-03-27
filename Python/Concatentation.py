Name = input("Input name: ")
Surname = input("Input Surname: ")

while len(Name+Surname) > 20:
    print("The name is too long, please re-enter...")
    Name = input("Input name: ")
    Surname = input("Input Surname: ")

print(Name, Surname, len(Name+Surname))
