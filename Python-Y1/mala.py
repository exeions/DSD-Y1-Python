import time

e = ["f","a","r","r","e","l","l"]

name = ""

for char in e:
    name += char

for i in range(100):
    print(name)
    time.sleep(0.1)