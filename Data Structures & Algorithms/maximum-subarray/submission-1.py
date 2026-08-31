class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curSum = 0

        for i in range(0, len(nums)):
            if curSum <= 0:
                curSum = 0
            curSum += nums[i]
            max_sum = max(max_sum, curSum)
        return max_sum
