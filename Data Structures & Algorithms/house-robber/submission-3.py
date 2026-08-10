class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
    
        cache = [-1] * len(nums)

        def dfs(i):
            if i < 0:
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = max(nums[i] + dfs(i-2), dfs(i-1))
            return cache[i]

        return dfs(len(nums)-1)