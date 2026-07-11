class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def bt(path, used):
            if len(path) == len(nums):
                result.append(path[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                path.append(nums[i])

                bt(path, used)

                used[i] = False
                path.pop()

        bt([], [False] * len(nums))
        return result