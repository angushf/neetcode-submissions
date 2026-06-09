class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        mid = (0 + len(nums)-1) // 2

        if nums[mid] > nums[-1]:
            # smallest val is to the right
            return self.findMin(nums[mid+1:])
        else:
            # smallest val is to the left
            return self.findMin(nums[:mid+1])
