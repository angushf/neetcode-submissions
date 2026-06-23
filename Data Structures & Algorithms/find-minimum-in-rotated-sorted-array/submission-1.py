class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Bisect_left type of BS
        # Once we identify which of the two sorted runs our min is in
        # we can use bisect left to find min element

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            print(f"lo {lo}, hi {hi}")
            mid = (lo + hi) // 2

            if nums[mid] < nums[hi]:
                hi = mid
            else:
                lo = mid + 1

        return nums[lo]
