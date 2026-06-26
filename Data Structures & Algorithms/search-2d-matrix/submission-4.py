class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            midArr = (lo + hi) // 2

            if target < matrix[midArr][0]:
                hi = midArr - 1
            elif target > matrix[midArr][-1]:
                lo = midArr + 1
            else:
                lo1 = 0
                hi1 = len(matrix[midArr])

                while lo1 < hi1:
                    mid = (lo1 + hi1) // 2

                    if matrix[midArr][mid] < target:
                        lo1 = mid + 1
                    else:
                        hi1 = mid

                return True if lo1 < len(matrix[midArr]) and matrix[midArr][lo1] == target else False

        return False