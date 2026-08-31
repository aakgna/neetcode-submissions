class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = dict()
        for w in strs:
            vals = [0] * 26
            base = ord('a')
            for l in w:
                vals[ord(l) - base] += 1
            if tuple(vals) in res:
                res[tuple(vals)].append(w)
            else:
                res[tuple(vals)] = [w]
        return list(res.values())