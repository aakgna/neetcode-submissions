class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair = dict()
        for i in range(len(nums)):
            res = target - nums[i]
            if res in pair:
                return [pair[res], i]
            else:
                pair[nums[i]] = i
        return None