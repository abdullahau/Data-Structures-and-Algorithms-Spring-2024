class QuickList:
    def __init__(self, t):
        self.list = t
        self.pointer = 0
        self.length = len(t)

    def move(self, k):
        self.pointer += k

    def get(self, i):
        x = (i + self.pointer) % self.length
        return self.list[x]