class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_cnt = 0
        product = 1
        for n in nums:
            if n == 0:
                zero_cnt += 1
                continue
            product *= n
        if zero_cnt > 1:
            return [0] * len(nums)
        elif zero_cnt == 1:
            res = []
            for n in nums:
                if n == 0:
                    res.append(product)
                    continue
                res.append(0)
            return res
        else:
            res = []
            for n in nums:
                res.append(product//n)
            return res
        return []