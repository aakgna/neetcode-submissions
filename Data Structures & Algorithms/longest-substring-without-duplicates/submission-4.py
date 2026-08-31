class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        unique = set()
        i, j = 0, 0
        best = 1
        while j < len(s):
            if s[j] in unique:
                print("removed", s[i], unique)
                unique.remove(s[i])
                i += 1
            else:
                print("added", s[j], unique)
                val = j-i+1
                best = max(best, val)
                unique.add(s[j])
                j += 1
        return best