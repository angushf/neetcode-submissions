class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Read/Write pointers
        # Condition = nums[r] != 0
        # When condition is true we swap nums[r] with nums[w]
        # cuz index w represents the next available spot in the array

        write = 0

        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1

        return nums
