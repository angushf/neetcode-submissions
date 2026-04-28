class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixArr = [nums[0]]
        suffixArr = [nums[-1]]
        result = []

        for i in range(1, len(nums)):
            prefixSum = prefixArr[i-1] * nums[i]
            prefixArr.append(prefixSum)

        for i in range(len(nums)-2, -1, -1):
            suffixSum = suffixArr[0] * nums[i]
            suffixArr.insert(0, suffixSum)
        

        for i in range(0, len(nums)):
            if i == 0:
                result.append(suffixArr[i+1])
            elif i == len(nums)-1:
                result.append(prefixArr[i-1])
            else:
                product = prefixArr[i-1] * suffixArr[i+1]
                result.append(product)

        return result
        