name = input("Input your name: ")
length = len(name)

print(length), "is the length of your name"

age = input("Input age: ")

if age == length:
    print("your age is the same length of your name!")
else:
    print(f"you are {age}")

score = float(input("Input test score: "))
passed = False

if score >= 100:
    res = "A*"
    print(res)
    passed = True
elif score >= 80:
    res = "A"
    print(res)
    passed = True   
elif score >= 60:
    res = "B"
    print(res)
    passed = True
elif score >= 40:
    res = "C"
    print(res)
    passed = True
elif score >= 20:
    res = "D"
    print(res)
    passed = True
elif score >= 0:
    res = "F"
    print(res)
    passed = False
else:

    print("Not allowed!!!!!!!")

if passed == True:
    res1 = "passed"
    print("You passed!")
else:
    res1 = "failed"
    print("You failed!")

print(f"Your name is {name} and your age is {age} your test score is {score} and you got a {res} and you {res1}")