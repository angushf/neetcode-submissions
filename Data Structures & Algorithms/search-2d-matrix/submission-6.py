class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Binary search to find row that target SHOULD exist in
        # Once we have found the row that should hold target, we then do a 
        # binary search on that row to see if we can find it and we'll
        # return True/False accordingly

        lo = 0
        hi = len(matrix) - 1

        while lo <= hi:
            midArr = (lo + hi) // 2

            if matrix[midArr][0] <= target <= matrix[midArr][-1]:
                # Target should exist in this row so do BS on it
                lo1 = 0
                hi1 = len(matrix[midArr]) - 1

                while lo1 <= hi1:
                    mid = (lo1 + hi1) // 2

                    if target == matrix[midArr][mid]:
                        return True
                    elif target < matrix[midArr][mid]:
                        hi1 = mid - 1
                    else:
                        lo1 = mid + 1

                return False


            elif target < matrix[midArr][0]:
                hi = midArr - 1
            else:
                lo = midArr + 1

        return False