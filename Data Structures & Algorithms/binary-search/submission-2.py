class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Classic BS template
        
        def binarySearch(lo, hi):
            if lo > hi:
                return -1

            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(lo, mid - 1)
            else:
                return binarySearch(mid + 1, hi)

        return binarySearch(0, len(nums) - 1)
