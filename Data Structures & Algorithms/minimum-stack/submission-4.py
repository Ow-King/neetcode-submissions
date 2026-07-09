class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = float('inf')
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        if val <= self.min_val:
            self.min_val = val
            self.min_stack.append(val)
        
        

    def pop(self) -> None:
        if self.stack.pop(len(self.stack) - 1) == self.min_stack[len(self.min_stack) - 1]:
            self.min_stack.pop(len(self.min_stack) - 1)
            if len(self.min_stack) == 0:
                self.min_val = float('inf')
            else:
                self.min_val = self.min_stack[len(self.min_stack) - 1]  

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

        
