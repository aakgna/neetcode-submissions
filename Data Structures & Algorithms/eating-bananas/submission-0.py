import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        largest = max(piles)
        l, r = 1, largest
        minimum = math.inf
        while l <= r:
            m = l + ((r-l) // 2)
            temph = h
            for p in piles:
                if p <= m:
                    temph -= 1
                else:
                    if p % m == 0:
                        temph -= p // m
                        continue
                    temph -= ((p // m) + 1)
            if temph >= 0 and m < minimum:
                minimum = m
                r = m - 1
            elif temph < 0:
                l = m + 1
            elif temph >= 0:
                r = m - 1
        print(minimum)
        return minimum