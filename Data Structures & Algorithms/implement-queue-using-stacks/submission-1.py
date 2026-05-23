class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self._reverseList(1)
        value = self.stack2.pop(-1)
        self._reverseList(2)
        return value

    def peek(self) -> int:
        self._reverseList(1)
        value = self.stack2[-1]
        self._reverseList(2)
        return value

    def empty(self) -> bool:
        return len(self.stack1) == 0

    def _reverseList(self, num):
        if num == 1:
            while len(self.stack1) != 0:
                value = self.stack1.pop(-1)
                self.stack2.append(value)
        else:
            while len(self.stack2) != 0:
                value = self.stack2.pop(-1)
                self.stack1.append(value)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()