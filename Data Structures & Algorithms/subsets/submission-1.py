class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def bt(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                bt(i + 1, path)
                path.pop()

        bt(0, [])
        return result