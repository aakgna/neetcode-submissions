from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = 0
        perm = [0] * 26
        for letter in s1:
            perm[ord(letter) - ord('a')] += 1
        s2Count = [0] * 26
        for r in range(0, len(s2)):
            if r-l+1 <= len(s1):
                s2Count[ord(s2[r])-ord('a')] += 1
            else:
                s2Count[ord(s2[l])-ord('a')] -= 1
                s2Count[ord(s2[r])-ord('a')] += 1
                l += 1
            if perm == s2Count:
                return True
        print(s2Count)
        return False
            