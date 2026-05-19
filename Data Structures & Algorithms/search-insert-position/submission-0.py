class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       
        def binarySearch(startIndex, endIndex):
            if startIndex > endIndex:
                return startIndex

            mid = (startIndex + endIndex) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return binarySearch(startIndex, mid - 1)
            else:
                return binarySearch(mid + 1, endIndex)

        return binarySearch(0, len(nums) - 1)