class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        base = ord('a')
        groups = dict()

        for s in strs:
            unique = [0] * 26
            for l in s:
                unique[ord(l)-base] += 1
            tup = tuple(unique)
            if tup in groups:
                groups[tup].append(s)
            else:
                groups[tup] = [s]
        return list(groups.values())