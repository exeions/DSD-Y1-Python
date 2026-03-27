import random as rdm

randomNumber = rdm.random()

name = input("Input name: ")

with open("NamesNumbers.txt", "a") as file:
    file.write(f"{name} {str(randomNumber)}\n")

with open("NamesNumbers.txt", "r") as file:
    contents = file.read()
    lineCount = contents.count("\n")
    print(f"Total lines are {lineCount} lines.")
    print(contents.strip())