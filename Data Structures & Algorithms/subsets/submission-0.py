class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(start, path):
            if start == len(nums):
                result.append(path[:])
                return

            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i]) # [1]
                backtracking(i + 1, path)
                path.pop()


        backtracking(0, [])
        return result