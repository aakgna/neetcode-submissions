class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        m = 0
        if nums[l] < nums[r]:
            return nums[l]
        while l < r:
            m = (l+r) // 2
            print(m)
            if nums[m] > nums[l]:
                l = m
                m = (l+r) // 2
            elif nums[m] < nums[r]:
                r = m
                m = (l+r) // 2
            else:
                if l == r:
                    break
                l += 1
                m = (l+r) // 2
        print(m)
        return nums[m]