class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        order = set(nums)
        res = 1
        ans = []
        for n in order:
            if n-1 in order:
                continue

            val = n+1
            while True:
                if val not in order:
                    ans.append(res)
                    res = 1
                    break
                val += 1
                res += 1
        return max(ans)