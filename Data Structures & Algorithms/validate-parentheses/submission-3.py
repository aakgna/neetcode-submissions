class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        matching = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        if s[0] in matching.values():
            return False
        stack = []
        for char in s:
            if char in matching.keys():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if matching[val] != char:
                    return False
            print(stack)
        if len(stack) > 0:
            return False
        return True