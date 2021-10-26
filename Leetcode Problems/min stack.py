class MinStack:

    def __init__(self):
        self.arr = []


    def push(self, val: int) -> None:
        if len(self.arr):
            if val < self.arr[-1][0]:
                self.arr.append([val,[]])
            else: self.arr[-1][1].append(val)
        else: self.arr.append([val,[]])


    def pop(self) -> None:
        if self.arr[-1][1]:
            self.arr[-1][1].pop()
        else: self.arr.pop()


    def top(self) -> int:
        if len(self.arr[-1][1]):
            return self.arr[-1][1][-1]
        return self.arr[-1][0]


    def getMin(self) -> int:
        return self.arr[-1][0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()