class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for n in range(0, len(nums)):
            val = target - nums[n]
            if val in seen:
                return [seen[val], n]
            else:
                seen[nums[n]] = n
        return None