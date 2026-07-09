class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.size = 0
        self.min_size = 0
        self.min_val = float('inf')
        

    def push(self, val: int) -> None:
        self.size += 1
        self.stack.append(val)

        if val <= self.min_val:
            self.min_val = val
            self.min_size += 1
            self.min_stack.append(val)
        
        

    def pop(self) -> None:
        self.size -= 1
        if self.stack.pop(self.size) == self.min_stack[self.min_size - 1]:
            self.min_size -= 1
            self.min_stack.pop(self.min_size)
            if self.min_size == 0:
                self.min_val = float('inf')
            else:
                self.min_val = self.min_stack[self.min_size - 1]

    def top(self) -> int:
        return self.stack[self.size - 1]

    def getMin(self) -> int:
        return self.min_stack[self.min_size - 1]

        
