class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Iterate through nums and store complement:index in a map
        # At every element, check if (target - index) exists in map and if it does
        # you've found you answer - return [map[complement], index] as the index stored in map
        # will always be the first index found

        map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in map:
                return [map[complement], i]

            map[nums[i]] = i

        