class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = 0
        total = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                total += nums[i]
            else:
                result = max(result, total)
                total = nums[i]

        result = max(result, total)

        return result