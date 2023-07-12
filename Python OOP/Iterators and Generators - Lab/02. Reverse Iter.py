class  reverse_iter:
    def __init__(self, nums):
        self.nums = nums
        self.start = len(self.nums)
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            self.start -= 1
            return self.nums[self.start]
        else:
            raise StopIteration
