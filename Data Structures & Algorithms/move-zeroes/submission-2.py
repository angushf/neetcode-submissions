class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # read/write pointers
        # condition is check if read pointer != 0, then swap nums[r] with nums[w] and increment write pointer

        w = 0

        for r in range(len(nums)):
            if nums[r] != 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1

        