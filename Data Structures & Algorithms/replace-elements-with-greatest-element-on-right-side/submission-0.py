class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        for i in range(len(arr)):
            maxNum = 0
            for j in range(i+1, len(arr)):
                maxNum = max(maxNum, arr[j])
            arr[i] = maxNum

        arr[-1] = -1

        return arr