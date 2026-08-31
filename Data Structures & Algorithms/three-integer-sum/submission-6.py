class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        visited = set()
        res = list()
        for i in range(len(nums)):
            val1 = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                val2, val3 = nums[l], nums[r]
                target = val1 + val2 + val3
                if target == 0:
                    if (val1, val2, val3) not in visited:
                        res.append([val1, val2, val3])
                        visited.add((val1, val2, val3))
                    if nums[r] == nums[r-1]:
                        r -= 1
                    elif nums[l] == nums[l+1]:
                        l += 1
                    else:
                        l += 1
                elif target > 0:
                    r -= 1
                else:
                    l += 1
        return res