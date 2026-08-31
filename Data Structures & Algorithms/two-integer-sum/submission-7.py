class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = dict()

        for i in range(len(nums)):
            val = target - nums[i]
            if val in mem:
                return [mem[val], i]
            else:
                mem[nums[i]] = i
        return []