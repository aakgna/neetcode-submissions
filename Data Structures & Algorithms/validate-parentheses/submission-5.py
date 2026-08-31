class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        matching = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for l in s:
            if l in matching.keys():
                stack.append(l)
            elif len(stack) == 0 and l in matching.values():
                return False
            elif l != matching[stack.pop()]:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
                