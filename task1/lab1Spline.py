import scipy as sp
import scipy.interpolate as interpolate
import matplotlib.pyplot as plt


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


x = getxst(10)
y = testfunction(x)
xnew = getxst(100)
f1 = interpolate.interp1d(x, y, kind='linear')
f2 = interpolate.interp1d(x, y, kind='cubic')
plt.plot(x, y, 'ro')
plt.plot(xnew, f1(xnew), 'g--')
plt.plot(xnew, f2(xnew), 'c-')
plt.grid(True)
plt.legend(['data', 'linear', 'cubic'])
plt.show()
