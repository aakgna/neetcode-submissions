class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        has = set()
        res = list()
        for i in range(len(nums)-2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if (nums[i], nums[l], nums[r]) in has:
                    l += 1
                    continue
                val = nums[i] + nums[l] + nums[r]
                if val == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    has.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif val > 0:
                    r -= 1
                else:
                    l += 1
        return res
