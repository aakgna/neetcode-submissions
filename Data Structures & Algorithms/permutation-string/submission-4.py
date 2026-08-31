class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        tup1 = [0] * 26
        val_a = ord('a')
        for l in s1:
            tup1[ord(l) - val_a] += 1
        print(tup1)
        i = len(s1)
        tup2 = [0] * 26
        for l in s2[:i]:
            tup2[ord(l) - val_a] += 1
        if tup1 == tup2:
            return True
        print(tup2)
        while i < len(s2):
            if tup1 == tup2:
                return True
            start = i - len(s1)
            tup2[ord(s2[start]) - val_a] -= 1
            tup2[ord(s2[i]) - val_a] += 1
            print(tup2)
            i += 1
        if tup1 == tup2:
            return True
        return False