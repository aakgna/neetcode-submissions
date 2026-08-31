class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = ord("a")
        w1 = [0] * 26
        w2 = [0] * 26
        for l in s:
            w1[ord(l) - first] += 1
        for l in t:
            w2[ord(l) - first] += 1
        return tuple(w1) == tuple(w2)