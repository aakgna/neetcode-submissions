class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = 1
        seen = dict(sorted(seen.items(), key=lambda item: item[1], reverse=True))
        return list(seen.keys())[:k]