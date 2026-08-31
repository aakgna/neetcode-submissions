class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_S = dict()
        count_T = dict()
        for char_s, char_t in zip(s,t):
            count_S[char_s] = 1 + count_S.get(char_s,0)
            count_T[char_t] = 1 + count_T.get(char_t,0)
        return count_T == count_S