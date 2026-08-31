class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        index = -1
        product = 1
        if nums[0] == 0:
            zeroes += 1
        else:
            product *= nums[0]
        for n in range(1, len(nums)):
            if nums[n] == 0:
                zeroes += 1
                index = n
            else:
                product *= nums[n]
        if zeroes > 1:
            return [0] * len(nums)
        elif zeroes == 1:
            res = [0] * len(nums)
            res[index] = int(product)
        else:
            res = [0] * len(nums)
            for n in range(len(nums)):
                res[n] = int(product / nums[n])
        return res