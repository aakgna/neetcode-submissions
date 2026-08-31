class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        idx = []
        prod = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1
                idx.append(i)

        if zeroes > 1:
            return [0] * len(nums)
        elif zeroes == 1:
            for i in range(len(nums)):
                if i in idx:
                    continue
                prod *= nums[i]
            res = [0] * len(nums)
            res[idx[0]] = prod
            return res
        else:
            for n in nums:
                prod *= n
            res = [0] * len(nums)
            for i in range(len(nums)):
                res[i] = int(prod / nums[i])
            return res
