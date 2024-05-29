class Mex:
    def __init__(self):
        self.nums = set()
        self.mex = 0

    def add(self, x):
        self.nums.add(x)
        
        if self.mex in self.nums:
            return self.gen()
        else:
            return self.mex
    
    def gen(self):
        while self.mex in self.nums:
            self.mex += 1
        return self.mex