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

    def rotateAlpha(self, p1, alpha):
        return Point((self.x - p1.x) * math.cos(alpha)-(self.y - p1.y) * math.sin(alpha) + p1.x,
                     (self.x - p1.x) * math.sin(alpha)+(self.y - p1.y) * math.cos(alpha) + p1.y)
    
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
    
    def perpendicularLine(self, point):
        return Line(self.b, -self.a, self.a * point.y - self.b * point.x)

    def parallelLine(self, point):
        return Line(self.a, self.b, -self.a * point.x - self.b * point.y)

    def projectionLength(self, p1, p2):
        nearP1 = self.nearPoint(p1)
        nearP2 = self.nearPoint(p2)
        return sqrt((nearP1.x - nearP2.x)**2 + (nearP1.y - nearP2.y)**2)

    def middlePoint(self, p1):
        nearP1 = self.nearPoint(p1)
        v1 = nearP1 - p1
        return Point(p1.x + v1.x/2, p1.y + v1.y/2)

    def symmetricPoint(self, p1):
        nearP1 = self.nearPoint(p1)
        v1 = nearP1 - p1
        return Point(p1.x + v1.x*2, p1.y + v1.y*2)

    def insideTreug(self, p1):
        nearP1 = self.nearPoint(p1)
        v1 = nearP1 - p1
        if (v1.x * nearP1.x >= 0 and v1.y * nearP1.y >= 0) and(p1.x * nearP1.x >= 0 and p1.y * nearP1.y >= 0):
            return True
        else:
            return False

    def rotatedLine(self, p1):
        hp1 = Point(0, -self.c/self.b)
        hp2 = Point(1, -(self.a + self.c)/self.b)
        new1 = Point((hp1.y - p1.y) + p1.x, -(hp1.x - p1.x) + p1.y)
        new2 = Point((hp2.y - p1.y) + p1.x, -(hp2.x - p1.x) + p1.y)
        return Line.fromCoord(new2.x, new2.y, new1.x, new1.y)

    def rotatedAlpha(self, p1, alpha):
        hp1 = Point(0, -self.c/self.b)
        hp2 = Point(1, -(self.a + self.c)/self.b)
        new1 = hp1.rotateAlpha(p1, alpha)
        new2 = hp2.rotateAlpha(p1, alpha)
        return Line.fromCoord(new2.x, new2.y, new1.x, new1.y)

    def bisectrix(self, other):
        if self.isParallel(other.perpendicularLine(Point(0,0))):
            return None
        elif self.isParallel(other):
            hp1 = Point(0, -other.c/other.b)
            hp2 = Point(1, -(other.a + other.c)/other.b)
            mid1 = self.middlePoint(hp1)
            mid2 = self.middlePoint(hp2)
            ans = Line.fromCoord(mid2.x, mid2.y, mid1.x, mid1.y)
            ans.normalize()
            return ans
        else:
            interP = self.intersection(other)
            k1 = -self.a/self.b
            k2 = -other.a/other.b
            print(k1, k2)
            tan = abs((k1-k2)/(1 + k1 * k2))
            angle = math.atan(tan)/2
            if (k1 > 0 and k2 > 0 and k1 > k2) or (k1 < 0 and k2 < 0 and k1 > k2) or (k2 < 0 and k1 > 0):
                ans = other.rotatedAlpha(interP, angle)
                ans.normalize()
                return ans
            else:
                ans = self.rotatedAlpha(interP, angle)
                ans.normalize()
                return ans
        
    
p2 = Point(0,0)
p1 = Point(7.62, 1.11)
x = Line.fromCoord(1.19, -5.28, -14.60, -0.86)
y = Line.fromCoord(14.29, -1.73, -14.37, 5.14)
z = Line.fromCoord(0, 6, 0, -7.25)
print(x)
print(x.bisectrix(y))
