class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        res = [[] for i in range(len(nums) + 1)]
        for key, val in counts.items():
            res[val].append(key)
        final = []
        for i in range(len(res)-1, 0, -1):
            for num in res[i]:
                final.append(num)
                if len(final) == k:
                    return final