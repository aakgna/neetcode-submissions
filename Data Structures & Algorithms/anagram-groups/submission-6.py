class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = dict()
        for s in strs:
            res = [0] * 26
            for l in s:
                res[ord(l) - ord('a')] += 1
            res = tuple(res)
            if res not in buckets:
                buckets[res] = [s]
            else:
                buckets[res].append(s)
        return buckets.values()