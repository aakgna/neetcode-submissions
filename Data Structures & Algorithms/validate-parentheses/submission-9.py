class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            '}': "{",
            ']': '[',
            ')': '('
        }
        stack = list()
        for l in s:
            if l in pairs.keys():
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if val != pairs[l]:
                    return False
            else:
                stack.append(l)
        if len(stack) > 0:
            return False
        return True