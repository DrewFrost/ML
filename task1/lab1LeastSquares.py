import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from scipy.optimize import fsolve


def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


def getxst(num):
    xvalst = []
    for i in range(1, num + 1):
        x = 4 * (i - 1) / (num - 1) - 2
        xvalst.append(x)
    return (xvalst)


def testfunction(x):
    y = []
    for xi in x:
        y.append(1 / (1 + 25 * xi ** 2))
    return y


def getxt(num):
    xvalt = []
    for i in range(1, num):
        x = 4 * (i - 0.5) / (num - 1) - 2
        xvalt.append(x)
    return (xvalt)


n = int(input("Enter number of points: "))
grade = int(input("Enter grade: "))

limB = -2
limE = 2

x = np.linspace(limB, limE, n)
y = 1 / (1 + 25 * x * x)

xst = getxst(n)
yst = testfunction(xst)
xt = getxt(n)
yt = testfunction(xt)

plt.scatter(x, y)
plt.scatter(xt, yt)

legend = []

fx = sp.linspace(x[0], x[-1], 1000)
fx1 = sp.linspace(xst[0], x[-1], 1000)


def loss(y1, y2):
    return (y1 - y2) ** 2


fp, residuals, rank, sv, rcond = sp.polyfit(x, y, grade, full=True)

f = sp.poly1d(fp)

plt.plot(fx, f(fx), 'r-', linewidth=1)
legend.append("grade={}".format(grade))
f2 = f - 1000
t = fsolve(f2, x[-1])

total_loss = sum([loss(y[i], f(fx[i])) for i in range(x.shape[0])])

print("Емпіричний ризик:")
print(total_loss)

plt.legend(legend, loc="upper left")
plt.grid()
plt.show()
