class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False
        l, r = 0, len(matrix) - 1
        m = 0
        while r > l:
            m = (l + r) // 2
            if matrix[m][-1] < target:
                l = m + 1
                m = (l + r) // 2
            else:
                r = m
                m = (l + r) // 2
        l, r = 0, len(matrix[m]) - 1
        while l <= r:
            m2 = (l + r) // 2
            print(matrix[m][m2])
            if matrix[m][m2] > target:
                r = m2 - 1
            elif matrix[m][m2] < target:
                l = m2 + 1
            else:
                return True
        return False