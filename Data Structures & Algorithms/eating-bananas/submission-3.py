import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        smallest, biggest = 1, max(piles)
        hours = h
        m = (smallest + biggest) // 2
        while smallest != biggest:
            m = (smallest + biggest) // 2
            for p in piles:
                ans = int(math.ceil(p / m))
                hours -= ans
            if hours > 0:
                biggest = m
            elif hours < 0:
                smallest = m + 1
            else:
                biggest = m
            hours = h
        return smallest