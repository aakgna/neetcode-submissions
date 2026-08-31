class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = -1
        l, r = 0, len(heights) - 1

        while l < r:
            if heights[r] < heights[l]:
                best = max(best, (r-l)*heights[r])
                r -= 1
            elif heights[l] < heights[r]:
                best = max(best, (r-l)*heights[l])
                l += 1
            else:
                best = max(best, (r-l)*heights[l])
                if heights[r-1] < heights[l+1]:
                    l += 1
                elif heights[r-1] > heights[l+1]:
                    r -= 1
                else:
                    l += 1
                    r -= 1
        return best