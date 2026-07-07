class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lo = 0
        hi = len(matrix) * len(matrix[0]) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            row, col = mid // len(matrix[0]), mid % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False