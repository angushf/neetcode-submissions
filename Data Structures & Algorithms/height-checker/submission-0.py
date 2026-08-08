class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sorted_arr = sorted(heights)
        result = 0
        for i in range(len(heights)):
            if heights[i] != sorted_arr[i]:
                result += 1

        return result