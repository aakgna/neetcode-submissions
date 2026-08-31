class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = dict()
        for w in strs:
            pattern = [0] * 26
            val = ord("a")
            for l in w:
                pattern[ord(l) - val] += 1
            tup = tuple(pattern)
            if tup in groups:
                groups[tup].append(w)
            else:
                groups[tup] = [w]
        return list(groups.values())