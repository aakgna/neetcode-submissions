class Solution:
    def rob(self, nums: List[int]) -> int:
        max_num = nums[0]
        for i in range(2, len(nums)):
            max_num = max(max_num, nums[i-2])
            nums[i] += max_num
        length = len(nums) - 1
        return max(nums[length], nums[length-1])