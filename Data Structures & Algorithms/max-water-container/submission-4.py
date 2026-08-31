class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        total = 0
        while i < j:
            val = (j-i) * min(heights[i], heights[j])
            if val > total:
                total = val
            if heights[i] >= heights[j]:
                j -= 1
            elif heights[i] < heights[j]:
                i += 1
        return total