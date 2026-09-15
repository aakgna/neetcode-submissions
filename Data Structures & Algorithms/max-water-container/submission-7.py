class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0

        while l < r:
            if heights[l] < heights[r]:
                best = max(best, (r-l)*heights[l])
                l += 1
            elif heights[r] < heights[l]:
                best = max(best, (r-l)*heights[r])
                r -= 1
            else:
                best = max(best, (r-l)*heights[r])
                l += 1
                r -= 1
        return best