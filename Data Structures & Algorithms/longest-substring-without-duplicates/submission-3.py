class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        seen = set()
        i, j = 0, 0
        res = 0
        while j < len(s):
            if s[j] in seen:
                res = max(j-i, res)
                seen.remove(s[i])
                i += 1
            else:
                seen.add(s[j])
                j += 1
        return max(res, len(seen))
                