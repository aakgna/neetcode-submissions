class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = dict()
        for i in range(len(nums)):
            if nums[i] in pair:
                return [pair[nums[i]], i]
            x = target - nums[i]
            pair[x] = i
