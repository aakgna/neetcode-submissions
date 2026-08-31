class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_S = dict()
        count_T = dict()
        for char in s:
            count_S[char] = 1 + count_S.get(char,0)
        for char in t:
            count_T[char] = 1 + count_T.get(char,0)
        return count_T == count_S