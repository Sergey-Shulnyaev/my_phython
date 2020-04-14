class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def __str__(self):
        if self.a < 0:
            a = " - %.2fx" % (-self.a)
        else:
            a = "%.2fx" % (self.a)
        if self.b < 0:
            b = " - %.2fx" % (-self.b)
        else:
            b = " + %.2fx" % (self.b)
        if self.c < 0:
            c = " - %.2fx" % (-self.c)
        else:
            c = " + %.2fx" % (self.c)
        return a + b + c + " = 0"
    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1 - y2, x2 - x1, x1 * y2 - x2 * y1)
    

s = Line(3,4,5)
x = Line.fromCoord(1, 2, 3, 4)
print(s)
print(x)
