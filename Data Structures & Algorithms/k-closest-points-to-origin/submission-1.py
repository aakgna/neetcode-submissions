import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            val = math.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)
            tup = (val, p)

            heapq.heappush(heap, tup)

        res = list()

        for i in range(0, k):
            t, a = heapq.heappop(heap)
            res.append(a)
        return res