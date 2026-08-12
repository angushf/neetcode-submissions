class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def dfs(i):
            if i == len(nums):
                return 0

            if cache[i] != -1:
                return cache[i]

            count = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    count = max(1 + dfs(j), count)
               

            cache[i] = count
            return cache[i]
                    

        return max(dfs(i) for i in range(len(nums)))
