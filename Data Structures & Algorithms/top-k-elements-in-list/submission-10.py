import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = dict()
        for n in nums:
            if n in seen:
                seen[n] += 1
            else:
                seen[n] = 1
        rev = dict()
        heap = list()
        for key, val in seen.items():
            if -val not in rev:
                rev[-val] = [key]
                heapq.heappush(heap, -val)
            else:
                rev[-val].append(key)
        res_idx = list()
        for i in range(0,k):
            if len(heap) == 0:
                break
            num = heapq.heappop(heap)
            res_idx.append(num)
        res = list()
        for val in res_idx:
            keys = rev[val]
            for l in keys:

                res.append(l)
                if len(res) == k:
                    return res
        return res