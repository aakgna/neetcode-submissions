class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack = [[],[nums[0]]]
        for i in range(1, len(nums)):
            temp = list()
            for el in stack:
                cop = el.copy()
                temp.append(el)
                cop.append(nums[i])
                temp.append(cop)
            stack = temp
        return stack