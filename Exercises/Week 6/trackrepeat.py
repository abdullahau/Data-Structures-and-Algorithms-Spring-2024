class TrackRepeat:
    def __init__(self):
        self.nums = {}
        self.repeats = {}
        self.repeated_nums = 0

    def add(self, x, k):
        past_count = 0
        if x in self.nums:
            past_count = self.nums[x]
        else:
            self.nums[x] = 0
        self.nums[x] += k
        
        new_count = past_count + k
    
        if past_count > 0:
            if past_count in self.repeats:
                self.repeats[past_count] -= 1
            if self.repeats[past_count] >= 1:
                self.repeated_nums -= 1
        
        if new_count in self.repeats:        
            self.repeats[new_count] += 1
            if self.repeats[new_count] > 1:
                self.repeated_nums += 1
        else:
            self.repeats[new_count] = 1
        
    def check(self):
        return False if self.repeated_nums > 0 else True