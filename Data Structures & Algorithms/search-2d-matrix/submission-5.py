class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                lo1 = 0
                hi1 = len(matrix[mid]) - 1

                while lo1 <= hi1:
                    mid1 = (lo1 + hi1) // 2

                    if matrix[mid][mid1] == target:
                        return True
                    elif matrix[mid][mid1] > target:
                        hi1 = mid1 - 1
                    else:
                        lo1 = mid1 + 1

                return False

            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1

        return False
