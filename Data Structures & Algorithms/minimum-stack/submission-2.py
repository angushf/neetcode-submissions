class MinStack:

    def __init__(self):
        self.stack = []
        self.minValue = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minValue) == 0:
            self.minValue.append(val)
        else:
            if self.minValue[-1] >= val:
                self.minValue.append(val)
        

    def pop(self) -> None:
        if self.minValue[-1] == self.stack[-1]:
            self.minValue.pop()
        self.stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minValue[-1]
        
