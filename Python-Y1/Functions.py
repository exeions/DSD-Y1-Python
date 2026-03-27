def test(a, b):
    calc = a + b
    
    return calc


print(test(6, 7))


def test2(a, b, c):
    division = (a/b)/c

    return division

print(test2(6,7,8))

list1 = ["malachi"]

def addList(x):
    e = input("Add input: ")
    x.append(e)    
    print(list1)

addList(list1)

