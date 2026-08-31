class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        freq = dict()

        for r in range(len(s)):
            if s[r] not in freq:
                freq[s[r]] = 1
            else:
                freq[s[r]] += 1
            if (r-l+1) - max(freq.values()) <= k:
                res = max(res, r-l+1)
            else:
                freq[s[l]] -= 1
                l += 1 
        return res