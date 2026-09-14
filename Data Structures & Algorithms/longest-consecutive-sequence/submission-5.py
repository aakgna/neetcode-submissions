class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        short = set(nums)
        best = 0    
        i = len(nums) - 1

        while i > -1:
            if nums[i] - 1 in short:
                i -= 1
                continue
            curr = 1
            val = nums[i]
            while val + 1 in short:
                curr += 1
                val += 1
            best = max(best, curr)
            i -= 1
        return best
