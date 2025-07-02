import numpy as np
from matplotlib import pyplot as plt

# window, graph = plt.subplots()
# plt.show()
#
# x = [2,5,8]
# y = [2,5,6]
# fig, ax = plt.subplots()
# ax.plot(x,y,color= 'blue',marker = 's')
# ax.set_xlabel("X time", fontsize=14)
# ax.set_ylabel("Y counts", fontsize=14)
# plt.show()

# -----------punktu grafiks----------
# window, graph = plt.subplots()
# plt.show()
#
# x = [2,5,8]
# y = [2,5,6]
# fig, ax = plt.subplots()
# ax.scatter(x, y, color='blue')
# ax.tick_params(axis='x', labelsize=16)
# ax.tick_params(axis='y', labelsize=16)
# plt.show()

# ---taskA-------------
# Duotas sąrašas x=[1,2,3,4,5,6,7,8,9] Viename lange, skirtinguose grafikuose
# atvaizduokite x kvadrate,x ⋅ 3,x ⋅ a, čia a - įvedamas vartotojo.
# Panaudokite skirtingas spalvas, linijų tipus.

x = np.array([1,2,3,4,5,6,7,8,9])
a = float(input("enter a: "))
fig, axs = plt.subplots(3, 1, figsize=(4, 8))

axs[0].plot(x, x**2, color='pink', linestyle='-', marker='s')
axs[0].set_title('x²')
axs[0].grid(True)

axs[1].plot(x, x*3, color='blue', linestyle='--', marker='s')
axs[1].set_title('x * 3')
axs[1].grid(True)

axs[2].plot(x, x*a, color='green', linestyle=':', marker='s')
axs[2].set_title(f'x * {a}')
axs[2].grid(True)

plt.tight_layout()
plt.show()
