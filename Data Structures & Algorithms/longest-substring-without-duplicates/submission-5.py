class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        l, r = 0, 0
        chars = set()

        while r < len(s):
            if s[r] not in chars:
                chars.add(s[r])
                best = max(best, r-l+1)
                r += 1
            else:
                chars.remove(s[l])
                l += 1
        return best