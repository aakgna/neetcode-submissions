class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        orig = dict()
        for n in nums:
            if n in orig:
                orig[n] +=1
            else:
                orig[n] = 0
        buckets = [[] for _ in range(len(nums))]

        for key, v in orig.items():
            buckets[v].append(key)

        res = []
        i = len(nums) - 1
        while i > -1:
            if k == 0:
                break
            if len(buckets[i]) > 0:
                res.append(buckets[i].pop())
                k -= 1
            else:
                i -= 1
        return res