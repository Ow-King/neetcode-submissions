class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        values = []

        for token in tokens:
            if token == '+':
                values.append(values.pop() + values.pop())
            elif token == '-':
                values.append(-(values.pop() - values.pop()))
            elif token == '*':
                values.append(values.pop() * values.pop())
            elif token == '/':
                a, b = values.pop(), values.pop()
                values.append(int(float(b) / a))
            else:
                values.append(int(token))
        return values[0]
        