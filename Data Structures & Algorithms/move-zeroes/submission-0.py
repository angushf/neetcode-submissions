class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # read/write pointers
        # keeper condition is write != 0
        # swap read and write

        write = 0

        for read, num in enumerate(nums):
            if num != 0:
                temp = nums[write]
                nums[write] = num
                nums[read] = temp
                write += 1

        return nums