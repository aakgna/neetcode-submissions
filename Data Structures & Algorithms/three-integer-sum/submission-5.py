class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        visited = set()
        nums.sort()

        for i in range(0, len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if 0 == nums[i] + nums[l] + nums[r] and (nums[i], nums[l], nums[r]) not in visited:
                    temp = [nums[i], nums[l], nums[r]]
                    res.append(temp)
                    visited.add(tuple(temp))
                    l += 1
                    r -= 1
                elif 0 < nums[i] + nums[l] + nums[r]:
                    r -= 1
                else:
                    l += 1
        return res