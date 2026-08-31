class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = dict()
        for i in range(0, len(numbers)):
            if target - numbers[i] in seen:
                return [seen[target - numbers[i]] + 1,i+1]
            if numbers[i] not in seen:
                seen[numbers[i]] = i
                
