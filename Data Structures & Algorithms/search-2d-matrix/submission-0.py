class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        outerL, outerR = 0, len(matrix) - 1

        while outerL <= outerR:
            outerm = outerL + ((outerR-outerL) // 2)
            temp = matrix[outerm]
            l, r = 0, len(temp) - 1
            m = l + ((r-l) // 2)
            while l <= r:
                m = l + ((r-l) // 2)
                if target < temp[m]:
                    r = m - 1
                elif target > temp[m]:
                    l = m + 1
                else:
                    return True
            if abs(m-l) < abs(m-r):
                outerR = outerm - 1
            else:
                outerL = outerm + 1
        return False