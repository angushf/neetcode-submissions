class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            l = i + 1 # left pointer
            r = len(nums) - 1 # right pointer
            while l < r:
                currSum = nums[l] + nums[r]
                target = abs(nums[i])
                if currSum == target:
                    arr = [nums[i], nums[l], nums[r]]
                    arr.sort()
                    result.append(arr)
                
                if currSum > target:
                    r -= 1
                else:
                    l += 1
        
        uniqueList = set(tuple(x) for x in result)
        return list(uniqueList)




