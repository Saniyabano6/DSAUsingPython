class MinStack(object):

    def __init__(self):
        self.stk = []
        self.minStk = []

    def push(self, value):
        self.stk.append(value)
        if not self.minStk or value <= self.minStk[-1]:
            self.minStk.append(value)
        else:
            self.minStk.append(self.minStk[-1])

    def pop(self):
        self.minStk.pop()
        return self.stk.pop()

    def top(self):
        return self.stk[-1]

    def getMin(self):
        return self.minStk[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()