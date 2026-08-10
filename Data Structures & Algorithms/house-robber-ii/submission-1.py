class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(nums):
            if len(nums) < 2:
                return nums[0]

            cache = [-1] * len(nums)

            def dfs(i):
                if i >= len(nums):
                    return 0

                if cache[i] != -1:
                    return cache[i]

                cache[i] = max(nums[i] + dfs(i+2), dfs(i+1))
                return cache[i]

            return dfs(0)

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))