class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)
        result = 0
        for i in range(len(nums)):

            if nums[i] - 1 in mySet:
                # not the start of sequence
                continue
            else:
                # start of sequence
                count = 1
                j = 1
                while nums[i] + j in mySet:
                    count += 1
                    j += 1
                result = max(result, count)

        return result
