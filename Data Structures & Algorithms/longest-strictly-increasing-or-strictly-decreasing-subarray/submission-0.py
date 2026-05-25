class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasingStack = []
        decreasingStack = []

        incCount = 0
        decCount = 0

        index = 0

        while index < len(nums):
            if decreasingStack and decreasingStack[-1] <= nums[index]:
                count = 0
                while decreasingStack:
                    decreasingStack.pop(-1)
                    count += 1

                decCount = max(decCount, count)

            if increasingStack and increasingStack[-1] >= nums[index]:
                count = 0
                while increasingStack:
                    increasingStack.pop(-1)
                    count += 1
                
                incCount = max(incCount, count)

            increasingStack.append(nums[index])
            decreasingStack.append(nums[index])
            index += 1
            
        return max(max(incCount, len(increasingStack)), max(decCount, len(decreasingStack)))