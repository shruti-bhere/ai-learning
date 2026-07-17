import matplotlib.pyplot as plt

x = [1,2,3,4]

y = [10,30,20,40]

plt.plot(x,y, marker="o", linestyle="--")

plt.grid(True)

plt.title("Styled Line Chart")

plt.show()