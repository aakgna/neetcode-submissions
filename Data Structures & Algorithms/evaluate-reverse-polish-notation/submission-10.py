class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for l in tokens:
            if l == '+':
                stack.append(stack.pop() + stack.pop())
            elif l == '-':
                r, l = stack.pop(), stack.pop()
                stack.append(l - r)
            elif l == '/':
                r, l = stack.pop(), stack.pop()
                stack.append(int(float(l)/ r))
            elif l == '*':
                stack.append(stack.pop() * stack.pop())
            else:
                stack.append(int(l))
            print(stack)
        return stack[0]