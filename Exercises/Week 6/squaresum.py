class SquareSum:
    def __init__(self):
        self.coord = []
        self.ysquare = 0
        self.xy = 0
        self.twoy = 0
        self.xsquare = 0
        self.x = 0

    def add(self, x, y):
        self.coord.append((x, y))
        self.ysquare += y**2
        self.xy -= 2*x*y
        self.twoy -= 2*y
        self.xsquare += x**2
        self.x += x

    def calc(self, a, b):
        return (self.ysquare + (self.xy * a) + (self.twoy * b) + (self.xsquare * (a)**2) + (self.x * 2 * a * b) + (len(self.coord) * b**2))