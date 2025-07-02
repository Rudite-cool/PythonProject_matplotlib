from matplotlib import pyplot as plt

window, graph = plt.subplots()
plt.show()

x = [2,5,8]
y = [2,5,6]
fig, ax = plt.subplots()
ax.plot(x,y,color= 'blue',marker = 's')
ax.set_xlabel("X time", fontsize=14)
ax.set_ylabel("Y counts", fontsize=14)
plt.show()


