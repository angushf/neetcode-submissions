class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binarySearch(start, end):

            def binarySearch2(start, end, array):
                if start > end:
                    return False

                mid = (start + end) // 2

                if target == matrix[array][mid]:
                    return True
                elif target < matrix[array][mid]:
                    return binarySearch2(start, mid - 1, array)
                else:
                    return binarySearch2(mid + 1, end, array)

            if start > end:
                return False

            mid = (start + end) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return binarySearch2(0, len(matrix[mid]) - 1, mid)
            elif target < matrix[mid][0]:
                return binarySearch(start, mid - 1)
            elif target > matrix[mid][-1]:
                return binarySearch(mid + 1, end)

        return binarySearch(0, len(matrix) - 1)



