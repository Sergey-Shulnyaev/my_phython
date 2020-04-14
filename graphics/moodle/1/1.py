import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%.2f, %.2f)" % (self.x, self.y)

s = Point(5.32542, 5.523432)
print(s)
