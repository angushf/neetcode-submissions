class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        running = 0

        seen = {0:1}

        for i, num in enumerate(nums):
            running += num
            count += seen.get(running - k, 0)
            seen[running] = seen.get(running, 0) + 1

        return count