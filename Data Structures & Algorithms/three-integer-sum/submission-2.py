class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        print(nums)
        combos = list()
        visited = dict()
        for i in range(0, len(nums) - 2):
            if nums[i] not in visited:
                visited[nums[i]] = True
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    current_sum = nums[i] + nums[j] + nums[k]
                    if current_sum == 0:
                        combos.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                        while j < k and nums[j] == nums[j-1]:
                            j += 1
                        while j < k and nums[k] == nums[k+1]:
                            k -= 1
                    elif current_sum > 0:
                        k -= 1
                    else:
                        j += 1
        return combos