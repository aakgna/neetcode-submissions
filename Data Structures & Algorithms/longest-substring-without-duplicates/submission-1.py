class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visits = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in visits:
                visits.remove(s[l])
                l += 1
            visits.add(s[r])
            res = max(res, r-l+1)
        return res