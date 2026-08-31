class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        stack = list()
        while i < len(tokens):
            if tokens[i] == "+":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1 + val2)
            elif tokens[i] == "-":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1 - val2)
            elif tokens[i] == "/":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1 / val2)
            elif tokens[i] == "*":
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                stack.append(val1 * val2)
            else:
                stack.append(int(tokens[i]))
            print(stack)
            i += 1
        return int(stack[0])