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

# x = np.array([1,2,3,4,5,6,7,8,9])
# a = float(input("enter a: "))
# fig, axs = plt.subplots(3, 1, figsize=(4, 8))
#
# axs[0].plot(x, x**2, color='pink', linestyle='-', marker='s')
# axs[0].set_title('x²')
# axs[0].grid(True)
#
# axs[1].plot(x, x*3, color='blue', linestyle='--', marker='s')
# axs[1].set_title('x * 3')
# axs[1].grid(True)
#
# axs[2].plot(x, x*a, color='green', linestyle=':', marker='s')
# axs[2].set_title(f'x * {a}')
# axs[2].grid(True)
# plt.tight_layout()
# plt.show()

# task2 -----Duoti sąrašai x = [1,2,3,4,5], y1=[2,2,0,0,2], y2 = [4,3,2,1,-1], y3 =
# [2,4,9,16,25], y4 = [-1,1,-1,1,-1]
# Atvaizduokite viename lange, skirtinguose grafikuose x~y1, x~y2,
# x~y3, x~y4 grafikus. Pirmasis grafikas - linijinis, antrasis - taškinis,
# trečiasis - linija su duomenų taškais, ketvirtasis - brūkšninis.
# Spalvos visų turi būti skirtingos. Grafikai, ašys turi turėti
# pavadinimus.

x = [1,2,3,4,5]
y1 = [2,2,0,0,2]
y2= [4,3,2,1,-1]
y3 = [2,4,9,16,25]
y4 = [-1,1,-1,1,-1]

fig, ax = plt.subplots()

plt.plot(x, y1,color= 'red',label='x~y1' )

ax.scatter(x, y2,color= 'blue', label='x~y2' )
ax.tick_params(axis='x')
ax.tick_params(axis='y')
ax.legend()

ax.plot(x,y3,color= 'pink',marker = '.',label='x~y3' )
ax.legend()

plt.plot(x, y4, color='black', linestyle='--',label='x~y4')
ax.legend()
plt.show()