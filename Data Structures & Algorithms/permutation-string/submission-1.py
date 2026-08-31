class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        orig = [0] * 26
        place = ord('a')
        for letter in s1:
            orig[ord(letter) - place] += 1
        l, r = 0, len(s1) - 1
        res = [0] * 26
        for i in range(l, r+1):
            res[ord(s2[i])-place] += 1
        while r < len(s2):
            if orig == res:
                return True
            res[ord(s2[l])-place] -= 1
            if r < len(s2) - 1:
                res[ord(s2[r+1])-place] += 1
            l += 1
            r += 1
        return False
