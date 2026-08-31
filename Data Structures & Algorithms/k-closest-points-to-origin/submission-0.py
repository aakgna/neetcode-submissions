import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res_val = [-math.inf] * k
        seen = {
            math.inf: [None] * k
        }
        for p in points:
            dist = (p[0]**2 + p[1]**2)**0.5
            val = heapq.heappop(res_val)
            if dist >= -val:
                heapq.heappush(res_val, val)
                continue
            if -val in seen and len(seen[-val]) > 0:
                seen[-val].pop()
                if len(seen[-val]) == 0:
                    del seen[-val]
            if dist in seen:
                seen[dist].append(p)
            else:
                seen[dist] = [p]
            heapq.heappush(res_val, -dist)
        res = []
        for val, key in seen.items():
            for k in key:
                res.append(k)
        return res