import matplotlib.pyplot as plt

x = [1,2,3,4]

y1 = [2,4,6,8]

y2 = [1,3,5,7]

plt.subplot(1,2,1)

plt.plot(x,y1)

plt.title("Graph 1")

plt.subplot(1,2,2)

plt.plot(x,y2)

plt.title("Graph 2")

plt.show()