import matplotlib.pyplot as plt
from Exp_of_basic_vs_method import *


x = UELocation

y1 = Record1

y2 = Record2


plt.plot(x, y1, label = "Always", marker = 'o')
plt.plot(x, y2, label = "Method", marker = 's') 

plt.title("always vs method")


plt.text(1, 1, f'Service Size: {Experiment.GetServiceSize()}', ha="right", va="top", transform=plt.gca().transAxes)
plt.xlabel("EdgeServerLocation")
plt.ylabel("Total Delay Time")

plt.legend()

plt.show()






