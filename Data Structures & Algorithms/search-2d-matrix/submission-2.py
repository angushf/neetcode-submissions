class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Classic BS cuz we're looking for target's existence in matrix

        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                lo = 0
                hi = len(matrix[mid]) - 1

                while lo <= hi:
                    j = (lo + hi) // 2

                    if matrix[mid][j] == target:
                        return True
                    elif matrix[mid][j] > target:
                        hi = j - 1
                    else:
                        lo = j + 1

            elif target < matrix[mid][0]:
                hi = mid - 1
            else:
                lo = mid + 1

        return False
