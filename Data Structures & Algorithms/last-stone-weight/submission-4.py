import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        res = []
        for val in stones:
            heapq.heappush(res, -val)
        
        while len(res) > 1:
            x = -heapq.heappop(res)
            y = -heapq.heappop(res)

            if x > y:
                heapq.heappush(res, -1 * (x - y))
            elif x < y:
                heapq.heappush(res, -1 * (y - x))
        if len(res) == 0:
            return 0
        return -res[0]
