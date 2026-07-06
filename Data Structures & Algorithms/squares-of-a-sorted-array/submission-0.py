class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        arr1 = []
        arr2 = []

        for i in range(len(nums)):
            val_squared = nums[i] ** 2
            if nums[i] < 0:
                arr1.insert(0, val_squared)
            else:
                arr2.append(val_squared)

        result = []

        l = 0
        r = 0
        
        while l < len(arr1) and r < len(arr2):
            smallest = None
            if arr1[l] <= arr2[r]:
                smallest = arr1[l]
                l += 1
            else:
                smallest = arr2[r]
                r += 1

            result.append(smallest)

        return result + arr1[l:] + arr2[r:] 

        