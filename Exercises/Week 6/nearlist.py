class NearList:
    def __init__(self, t):
        self.set = set(t)

    def find(self, x):
        if x in self.set:
            return x
        x_plus = x
        x_minus = x
        while True:
            x_minus -= 1
            x_plus += 1
            if x_minus in self.set:
                return x_minus
            if x_plus in self.set:
                return x_plus