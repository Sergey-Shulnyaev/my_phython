from math import sqrt
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)

    def distanceTo(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)

    def __sub__(self, other):
        return Point(math.floor((self.x - other.x) * 10000) / 10000, math.floor((self.y - other.y) * 10000) / 10000)

class Line:
    def __init__(self, a, b, c):
        if abs(a) < 0.0001:
            self.a = 0
        else:
            self.a = a
        if abs(b) < 0.0001:
            self.b = 0
        else:
            self.b = b
        if abs(c) < 0.0001:
            self.c = 0
        else:
            self.c = c
    def __str__(self):
        if self.a < 0:
            a = "-%.2fx" % (-self.a)
        else:
            a = "%.2fx" % (self.a)
        if self.b < 0:
            b = " - %.2fy" % (-self.b)
        else:
            b = " + %.2fy" % (self.b)
        if self.c < 0:
            c = " - %.2f" % (-self.c)
        else:
            c = " + %.2f" % (self.c)
        return a + b + c + " = 0"
    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1 - y2, x2 - x1, x1 * y2 - x2 * y1)
    
    def distanceToZero(self):
        return abs(self.c) / sqrt(self.a ** 2 + self.b ** 2)

    def distanceToPoint(self, point):
        return abs(self.a * point.x + self.b * point.y + self.c) / sqrt(self.a ** 2 + self.b ** 2)

    def isParallel(self, line):
        if abs(self.b * line.a - self.a * line.b) < 0.001:
            return True 
        else:
            return False

    def intersection(self, line):
        if self.isParallel(line):
            return None
        else:
            x = (line.c * self.b - self.c * line.b)/(line.b * self.a - self.b * line.a)
            y = (line.c * self.a - self.c * line.a)/(self.b * line.a - self.a * line.b)
            if abs(x) < 0.001:
                x = 0
            if abs(y) < 0.001:
                y =0
            p = Point(x, y)
            return p

    def nearPoint(self, point):
        oLine = Line(self.b, -self.a, self.a * point.y - self.b * point.x)
        return self.intersection(oLine)

    def oneSide(self, p1, p2):
        nearP1 = self.nearPoint(p1)
        nearP2 = self.nearPoint(p2)
        v1 = nearP1 - p1
        v2 = nearP2 - p2
        if v1.x * v2.x >= 0:
            return True
        else:
            return False

    def normalize(self):
        if self.c !=0:
            self.a = self.a/self.c
            self.b = self.b/self.c
            self.c = 1
        elif self.a != 0:
            self.b = self.b/self.a
            self.a = 1
        elif self.b != 0:
            self.b = 1
        return 0
    
    def perpendicularLine(self, point):
        return Line(self.b, -self.a, self.a * point.y - self.b * point.x)
        
p1 = Point(2,2)
p2 = Point(-6,-0.9999)
x = Line.fromCoord(0, 1, 1, 0)
y = Line.fromCoord(1, 0, 0, 1)
z = Line.fromCoord(0, 6, 0, -7.25)
print(x)
print(x.perpendicularLine(p1))
