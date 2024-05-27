class MaxList:
    def __init__(self):
        self.stack = []
        self.maximum = None
 
    def add(self, x):
        self.stack.append(x)
        if self.maximum != None:
            self.maximum = max(self.maximum, x)
        else:
            self.maximum = x
    
    def max(self):
        if self.maximum != None:
            return self.maximum