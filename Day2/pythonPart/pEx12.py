class pData():
    def __init__(self, name, num, size, mode):
        self.current = 0
        self.name = name
        self.num = num
        self.size = size
        self.mode = mode

    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.num:
            if self.mode == 1:
                return (self.name, self.num)
            else:
                return (self.num / 100)
        else:
            StopIteration
