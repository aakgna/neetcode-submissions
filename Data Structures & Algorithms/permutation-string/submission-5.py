class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        a1 = [0] * 26
        a2 = a1.copy()
        base = ord('a')
        for l in s1:
            a1[ord(l) - base] += 1
        i = 0
        while i < len(s1):
            a2[ord(s2[i]) - base] += 1
            i += 1
        l, r = 0, len(s1)-1
        while r < len(s2):
            print(a1, a2)
            if a1 == a2:
                return True
            else:
                a2[ord(s2[l]) - base] -= 1
                l += 1
                r += 1
                if r < len(s2):
                    a2[ord(s2[r]) - base] += 1
        return False
                
            