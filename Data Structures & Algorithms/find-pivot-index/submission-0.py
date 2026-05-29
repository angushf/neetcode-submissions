class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        result: List[tuple] = [[0, 0] for i in range(len(nums))]
        sum = 0

        # first pass: left to right
        for i, num in enumerate(nums):
            result[i][0] = sum

            sum += num

        sum = 0
        # second pass: right to left
        for i in range(len(nums) - 1, -1, -1):
            result[i][1] = sum

            sum += nums[i]

        print(result)

        # iterate over result and find tuple containing same numbers and return that tuple's index in result
        for i, arr in enumerate(result):
            if arr[0] == arr[1]:
                return i
        
        return -1