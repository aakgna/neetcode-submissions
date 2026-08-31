class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        order = set(nums)

        res = 0

        for n in order:
            if n-1 in order:
                continue
            if n+1 in order:
                res = max(res, 1)
            cnt = 1
            val = n + 1
            while True:
                if val in order:
                    cnt += 1
                else:
                    break
                val += 1
            res = max(res, cnt)
        return res