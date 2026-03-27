list1 = [1,7,3,8,55,78,32]

eTotal = 0
oTotal = 0

for i in list1:
    if i%2 == 0:
        print("Even")
        eTotal = i+eTotal
    else:
        print("Odd")
        oTotal = i+oTotal

print(eTotal, oTotal)

list2 = [(2,7), (7,3), (8,3)]

for x, y in list2:
    print(f"{x= } {y= }")



