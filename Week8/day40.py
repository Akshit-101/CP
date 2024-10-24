class MinStack:
    def __init__(self):
        self.st = []
        self.mini = float('inf')

    def push(self, value: int) -> None:
        val = value
        if not self.st:
            self.mini = val
            self.st.append(val)
        else:
            if val < self.mini:
                self.st.append(2 * val - self.mini)
                self.mini = val
            else:
                self.st.append(val)

    def pop(self) -> None:
        if not self.st:
            return
        el = self.st.pop()

        if el < self.mini:
            self.mini = 2 * self.mini - el

    def top(self) -> int:
        if not self.st:
            return -1

        el = self.st[-1]
        if el < self.mini:
            return self.mini
        return el

    def getMin(self) -> int:
        return self.mini


min_stack = MinStack()


min_stack.push(3)
min_stack.push(5)
print(min_stack.getMin())  # output: 3