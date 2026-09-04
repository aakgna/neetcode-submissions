class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []

        i = 0
        while i < len(tokens):
            if tokens[i] not in ["+", "-", "/", "*"]:
                stack.append(tokens[i])
                i += 1
                continue
            
            if tokens[i] == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left) + int(right))
            elif tokens[i] == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left) - int(right))
            elif tokens[i] == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(int(left) / int(right)))
            elif tokens[i] == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(int(left) * int(right)))
            i += 1
        if len(stack) == 1:
            return stack[0]
        else:
            return 0