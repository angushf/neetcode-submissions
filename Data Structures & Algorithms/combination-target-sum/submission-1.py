class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def bt(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                if remaining - nums[i] < 0:
                    continue

                path.append(nums[i])
                bt(i, remaining - nums[i], path)
                path.pop()

        bt(0, target, [])
        return result