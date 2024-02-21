import matplotlib.pyplot as plt
import numpy as np

range = float(input("range:"))
x = np.linspace(-range,range)

eq = input("funktion:")
y = eval(eq)



plt.plot(x,y)
plt.grid()
plt.show()