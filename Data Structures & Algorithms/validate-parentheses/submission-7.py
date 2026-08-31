class Solution:
    def isValid(self, s: str) -> bool:
        matches = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = list()
        keys = list(matches.keys())
        for l in s:
            if l in keys:
                stack.append(l)
            elif len(stack) == 0:
                return False
            elif matches[stack.pop()] != l:
                return False
        if len(stack) > 0:
            return False
        return True
                