import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

plt.style.use("dark_background") 
plt.title("Health Stats")

x = [1,2,3,4,5]
y = [6,7,8,9,10]

plt.subplot(1, 2, 1)
plt.xlabel("Average Pulse")
plt.ylabel("Caloire Burnage")
plt.grid()
plt.plot(x,y)

x = [1,2,3,4,5]
y = [6,1,12,15,21]

plt.subplot(1, 2, 2)
plt.xlabel("Average Time")
plt.ylabel("Money Spent")
plt.grid()
plt.plot(x,y)


plt.show()
