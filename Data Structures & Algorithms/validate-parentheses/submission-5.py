class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == '(':
                stack.append(1)
            elif c == '{':
                stack.append(2)
            elif c == '[':
                stack.append(3)
            elif (len(stack) == 0):
                return False
            elif c == ')':
                if (stack.pop() != 1):
                    return False
            elif c == '}':
                if (stack.pop() != 2):
                    return False
            elif c == ']':
                if (stack.pop() != 3):
                    return False
        
        if len(stack) > 0:
            return False

        return True