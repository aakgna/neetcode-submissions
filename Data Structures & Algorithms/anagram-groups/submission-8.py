class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = dict()
        for word in strs:
            temp = [0] * 26
            for l in word:
                temp[ord(l) - ord('a')] += 1
            comp = tuple(temp)
            if comp in buckets:
                buckets[comp].append(word)
            else:
                buckets[comp] = [word]
        return buckets.values()