import scipy as sp
import matplotlib.pyplot as plt


def error(f, x, y):
    return sp.sum((f(x) - y) ** 2)


def getxst(num):
    xvalst = []
    for i in range(1, num + 1):
        x = 4 * (i - 1) / (num - 1) - 2
        xvalst.append(x)
    return xvalst


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
    return xvalt


def lagranz(X, Y, K):
    S = 0
    for J in range(len(Y)):
        P1 = 1;
        P2 = 1
        for I in range(len(X)):
            if I == J:
                P1 = P1 * 1;
                P2 = P2 * 1
            else:
                P1 = P1 * (K - X[I])
                P2 = P2 * (X[J] - X[I])
        S = S + Y[J] * P1 / P2
    return S


points = 15
x = getxst(points)
xt = getxt(points)
y = testfunction(x)
yt = testfunction(xt)
Xnew = getxst(100)
Ynew = [lagranz(x, y, I) for I in Xnew]
# plt.plot(x,y,'ro',xt,yt,'bo',Xnew,Ynew,'y')
plt.plot(x, y, 'ro')
plt.plot(xt, yt, 'bo')
plt.plot(Xnew, Ynew, 'y')
plt.grid(True)
plt.legend(['Study points', 'Training Points', 'Lagrange'])
plt.show()
func = sp.poly1d(lagranz(xt, yt, 11))
