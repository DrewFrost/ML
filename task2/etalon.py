import matplotlib.pyplot as plt
import random


class Point:
    def __init__(self, x=0, y=0, classX=0, centroid=False):
        self.x = x
        self.y = y
        self.classX = classX
        self.centroid = centroid

    def getData(self):
        print("({0};{1} , [{2}])".format(self.x, self.y, self.classX))

    def distance(self, p):
        return ((self.x - p.x) ** 2 + (self.y - p.y) ** 2) ** (1 / 2)


def generateData(numberOfClassEl, classes):
    res = []
    for classN in classes:
        centerX, centerY = random.random() * 15.0, random.random() * 15.0
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


def getEtalons(train_data, classes):
    res = [[] for _ in range(len(classes))]
    resCentroids = [Point for _ in range(len(classes))]
    classNum = 0
    for cl in classes:
        for p in train_data:
            if p.classX == cl:
                res[classNum].append(p)
        classNum += 1
    for j in range(len(res)):
        p = getClosePoint(res[j])
        resCentroids[j] = p
        train_data[train_data.index(p)].centroid = True
    return resCentroids


def getClosePoint(class_points):
    res = [0 for _ in range(len(class_points))]
    for i in range(len(class_points)):
        p1 = class_points[i]
        for p2 in class_points:
            dist = p1.distance(p2)
            res[i] += dist
    return class_points[res.index(min(res))]


def findClasses(points, etalons):
    res = []
    for p in points:
        classX = getClassFromCentroid(etalons, p)
        pr = Point(p.x, p.y, classX)
        res.append(pr)
    return res


def getClassFromCentroid(etalons, point):
    res = []
    for et in etalons:
        res.append(point.distance(et))
    return etalons[res.index(min(res))].classX


def showData(class_points, bool=True):
    for i in class_points:
        if i.centroid:
            plt.plot(i.x, i.y, 'ro', color="Green")
        else:
            plt.plot(i.x, i.y, 'ro', color=i.classX)
    if bool:
        plt.show()
    return


def getError(test_p, res_p):
    j = 0
    for i in range(len(test_p)):
        if test_p[i].classX != res_p[i].classX:
            j += 1
    return 1 - j / len(all)


colors = ["Red", "Blue", "Yellow"]
all = generateData(30, colors)
st = 3
points_learn = getMyPoints(all, st)[0]
points_test = getMyPoints(all, st)[1]
plt.figure(figsize=(12, 9))
showData(points_learn, False)
for p in points_test:
    plt.plot(p.x, p.y, 'ro', color="Black")
plt.show()
etalons = getEtalons(points_learn, colors)
res = findClasses(points_test, etalons)
plt.figure(figsize=(12, 9))
showData(points_learn, False)
showData(res)
print(getError(points_test, res))
