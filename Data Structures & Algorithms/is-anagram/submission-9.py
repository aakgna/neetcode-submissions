class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        start = ord('a')
        buckets = [0] * 26
        for i in range(0, len(s)):
            buckets[ord(s[i]) - start] += 1
            buckets[ord(t[i]) - start] -= 1
        if buckets == ([0] * 26):
            return True
        return False