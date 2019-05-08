import matplotlib.pyplot as plt
import numpy as np
import random
import math
import copy


class Point:
    def __init__(self, x=0, y=0, classX=0):
        self.x = x
        self.y = y
        self.classX = classX

    def __str__(self):
        return ("({0};{1} , [{2}])".format(self.x, self.y, self.classX))

    def distance(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** (1 / 2)

def generateData(numberOfClassEl, classes):
    res = []
    for classN in classes:
        centerX, centerY = random.random() * 10.0, random.random() * 10.0
        for rowNum in range(numberOfClassEl):
            p = Point(random.gauss(centerX, 1), random.gauss(centerY, 1), classN)
            res.append(p)
    return res

def getMyPoints(all, val):
    res1 = []
    res2 = []
    for i in range(len(all)):
        if i % val == 0:
            res2.append(all[i])
        else:
            res1.append(all[i])
    return (res1, res2)


def showData(class_points, bool=True):
    for i in class_points:
        plt.plot(i.x, i.y, 'ro', color=i.classX)
    if bool:
        plt.show()
    return


def doParzen(point, trainData, h, yadro):
    res = {}
    for pt in trainData:
        col = point.distance(pt) / h
        res[pt] = yadro(col)
    return res


def getClass(neighbours, point):
    res = {}
    for key in neighbours:
        xClass = key.classX
        if xClass not in res:
            res[xClass] = 0
    votes = []
    for key in neighbours:
        cl = key.classX
        dist = neighbours[key]
        res[cl] += dist
    return max(res.items(), key=lambda x: x[1])


def makeParzen(points_test, points_learn, h, yadro):
    res = copy.deepcopy(points_test)
    for p in res:
        parz = doParzen(p, points_learn, h, yadro)
        p.classX = getClass(parz, p)[0]
    return res


def rectangle(param):
    if abs(param) <= 1:
        return 1/2
    else:
        return 0

def triangle(param):
    if abs(param) <= 1:
        return 1 - abs(param)
    else:
        return 0

def parabolic(param):
    if abs(param) <= 1:
        return 3/4*(1 - param ** 2)
    else:
        return 0

def square(param):
    if abs(param) <= 1:
        return 15/16*(1 - param ** 2) **  2
    return 0

def gaussian(param):
    if abs(param) <= 1:
        return (1/math.sqrt(2*np.pi))*math.exp((1/-2) * param ** 2)
    return 0

colors = ["Cyan", "Magenta", "Yellow"]
all = generateData(30, colors)
st = 3
points_learn = getMyPoints(all, st)[0]
points_test = getMyPoints(all, st)[1]
class_points = copy.deepcopy(points_test)
for i in range(len(class_points)):
    cl = class_points[i]
    cl.classX = "Gray"
    class_points[i] = cl
plt.figure(figsize=(12, 12))
showData(class_points, False)
showData(points_learn)

h = 0.5
res1 = makeParzen(class_points, points_learn, h, rectangle)
res2 = makeParzen(class_points, points_learn, h, triangle)
res3 = makeParzen(class_points, points_learn, h, parabolic)
res4 = makeParzen(class_points, points_learn, h, square)
res5 = makeParzen(class_points, points_learn, h, gaussian)
plt.figure("Rectangle")
showData(res1,False)
showData(points_learn)

plt.figure("Triangle")
showData(res2,False)
showData(points_learn)

plt.figure("Parabolic")
showData(res3,False)
showData(points_learn)

plt.figure("Square")
showData(res4,False)
showData(points_learn)

plt.figure("Gaussian")
showData(res5,False)
showData(points_learn)