class RepeatList:
    def __init__(self):
        self.nums = {}
        self.repeat = False

    def add(self, x):
        if x in self.nums:
            self.repeat = True
            self.nums[x] += 1
        else:
            self.nums[x] = 1

    def check(self):
        return self.repeat