from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%.2f/%.2f)" % (self.x, self.y)

    def distanceTo(self, point):
        return math.sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
        
        
class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
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

s = Point(3,2)
x = Line.fromCoord(1, 0, 0, 1)
print(s)
print(x.distanceToPoint(s))
