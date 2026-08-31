class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        freqs = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1
        
        for key, val in counts.items():
            freqs[val].append(key)
        tot = []
        for i in range(len(freqs) - 1, 0, -1):
            for n in freqs[i]:
                tot.append(n)
                if len(tot) == k:
                    return tot