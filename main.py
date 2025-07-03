from calendar import calendar

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

# x = [1,2,3,4,5]
# y1 = [2,2,0,0,2]
# y2= [4,3,2,1,-1]
# y3 = [2,4,9,16,25]
# y4 = [-1,1,-1,1,-1]
#
# fig, ax = plt.subplots()
#
# plt.plot(x, y1,color= 'red',label='x~y1' )
#
# ax.scatter(x, y2,color= 'blue', label='x~y2' )
# ax.tick_params(axis='x')
# ax.tick_params(axis='y')
# ax.legend()
#
# ax.plot(x,y3,color= 'pink',marker = '.',label='x~y3' )
# ax.legend()
#
# plt.plot(x, y4, color='black', linestyle='--',label='x~y4')
# ax.legend()
#
# ax.set_xlabel('time', fontsize=14)
# ax.set_ylabel('count', fontsize=14)
# plt.show()

# ----------task3-----Sugeneruoti sąrašą x, turintį 101 elementą (nuo 0 iki 100).
# Sukurti antrą sąrašą, kuriame būtų skaičiai, pakelti kvadratu, iš pirmojo sąrašo
# (x*x)Sukurti trečiąjį sąrašą, kuriame skaičiai būtų pakelti kvadratu ir
# padauginti iš atsitiktinai sugeneruoto skaičiaus (x*x)*a
# Sugeneruoti 100-to elementų ilgio sąrašą iš atsitiktinių skaičių.
# Visus šiuos sąrašus atvaizduoti grafike. Grafikas turi turėti
# pavadinimą, pavadintos ašys, pakeisti šriftų dydžiai.----------------

#
# x = np.arange(0, 101)
# y=x**2
# a= np.random.randn(101)
# y2= y * a
#
# plt.figure(figsize=(12, 6))
# fig, ax = plt.subplots()
#
# plt.plot(x, y, label='x²', linestyle='-', color='purple',)
# plt.plot(x, y2 , label='x² * a', linestyle='--', color='green')
# plt.plot(x, a, label='a (random)', linestyle=':', color='red')
#
# ax.legend()
# ax.set_xlabel("X time", fontsize=14)
# ax.set_ylabel("Y counts", fontsize=14)
# plt.show()

# -----------------------
# x = [1,2,3]
# y = [9,6,8]
# fig, ax = plt.subplots()
# ax.bar(x,y)
# plt.show()
# --------
# x = [1,2,3]
# y = [9,6,8]
# fig, ax = plt.subplots()
# ax.bar(x,y, color='green',
# label='gree')
# ax.set_xticks(x)
# ax.set_xticklabels(['Jan','Feb', 'Mar'])
# ax.set_ylabel('amount')
# ax.set_xlabel('months')
# ax.legend()
# plt.show()
# ----------------Turimos vidutinės mėnesių temparatūros
# tC=[-3.2, -3.2, +0.4, +6.7, +12.4, +15.4, +17.9, +17.1, +12.3,+7.2, +1.9, -1.9]
# Nubraižykite stulpelinę diagramą. Neigiamas temperatūras rodantys stulpeliai turi
# būti mėlyni, o teigiamas - žali. x ašyje turi būti rodomi mėnesių pavadinimai._______

# window, graph = plt.subplots()
# x = ['Jan','Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
# y=[-3.2, -3.2, +0.4, +6.7, +12.4, +15.4, +17.9, +17.1, +12.3,+7.2, +1.9, -1.9]
# fig, ax = plt.subplots()
# colors = ['blue' if y < 0 else 'green' for y in y]
# ax.bar(x, y, color= colors)
# ax.set_ylabel('Temp')
# ax.set_xlabel('months')
#
# plt.show()
# -----------------------------------
x = [1,2,3,5,8]
explode = [0,0,0,0,0.25]
fig, ax = plt.subplots()
ax.pie(x, labels=x,autopct='%1.2f%%')
plt.show()

# -------------