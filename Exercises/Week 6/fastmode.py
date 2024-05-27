class FastMode:
    def __init__(self):
        self.collection = {}
        self.most = (None, None)

    def add(self, x, k):
        if x not in self.collection:
            self.collection[x] = 0
        self.collection[x] += k 
        
        if self.most == (None, None):
            self.most = (k, -x)
        self.most = max(self.most, (self.collection[x], -x))

    def mode(self):
        return abs(self.most[1])