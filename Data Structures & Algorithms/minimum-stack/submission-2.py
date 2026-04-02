class MinStack:

    def __init__(self):
        self.s = []
        self.min_stack = []
        self.min_n = float("inf")

    def push(self, val: int) -> None:
        self.s.append(val)
        self.min_n = min(val, self.min_n)
        self.min_stack.append(self.min_n)
        

    def pop(self) -> None:
        self.min_stack.pop()
        if len(self.min_stack) > 0:
            self.min_n = self.min_stack[-1]
        else:
            self.min_n = float("inf")
        return self.s.pop()
        
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        

        
