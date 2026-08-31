class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        alpha = [0] * 26
        base = ord('A')
        i, j = 0, 0
        res = 1
        while j < len(s):
            alpha[ord(s[j]) - base] += 1
            big = max(alpha)
            rang = j - i + 1
            if rang - big <= k:
                res = max(res, rang)
                print(i, j, res)
                j += 1
            else:
                alpha[ord(s[i]) - base] -= 1
                i += 1
                j += 1
        return res