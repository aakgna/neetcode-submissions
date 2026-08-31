class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for n in range(len(nums)):
            needed = target - nums[n]
            if needed in seen:
                return [seen[needed], n]
            else:
                seen[nums[n]] = n
        return None