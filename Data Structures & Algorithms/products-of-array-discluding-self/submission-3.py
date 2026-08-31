class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zeros = 1, 0
        for n in nums:
            if n == 0:
                zeros += 1
            else:
                prod *= n
        if zeros > 1:
            return [0] * len(nums)
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            if zeros == 1:
                res[i] = 0 if nums[i] != 0 else int(prod)
                continue
            res[i] = int(prod/nums[i])
        return res