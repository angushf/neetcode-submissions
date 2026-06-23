class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Can use the classic BS pattern
        # We'll check to see if nums[mid] == target and return if so
        # if not, we'll have to choose one of the two sorted runs and run bs again

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < nums[hi]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
        
        return -1
                