class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = dict()
        base = ord('a')
        for s in strs:
            arr = [0] * 26
            for l in s:
                arr[ord(l) - base] += 1
            if tuple(arr) in buckets:
                buckets[tuple(arr)].append(s)
            else:
                buckets[tuple(arr)] = [s]
        return list(buckets.values())