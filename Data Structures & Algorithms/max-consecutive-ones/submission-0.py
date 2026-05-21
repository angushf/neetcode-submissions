class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        count = 0
        index = 0

        while index < len(nums):
            if nums[index] == 1:
                count += 1
                maxCount = max(maxCount, count)
            else:
                count = 0

            index += 1

        return maxCount
