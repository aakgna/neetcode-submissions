import math
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        best = -math.inf
        curr = 0
        i, j = 0, 0
        while j < len(nums):
            curr += nums[j]
            best = max(best, curr)
            if curr <= 0:
                curr = 0
                i += 1
                if i > j:
                    j = i
            else:
                j += 1
        return best