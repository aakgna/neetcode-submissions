class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = list()
        n = sorted(nums)
        for i in range(len(n) - 2):
            l, r = i + 1, len(n) - 1
            while l < r:
                if n[i] + n[l] + n[r] == 0 and [n[i],n[l],n[r]] not in res:
                    res.append([n[i],n[l],n[r]])
                    r -= 1
                    l  += 1
                elif n[i] + n[l] + n[r] > 0:
                    r -= 1
                elif n[i] + n[l] + n[r] < 0:
                    l += 1
                else:
                    l += 1
                    r -= 1
        return res