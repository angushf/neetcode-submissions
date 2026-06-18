class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # We will have one fixed pointer via a for loop and two converging pointers l & r
        # condition is nums[i] + nums[l] + nums[r] == 0
        # we add [nums[i], nums[l], nums[r]] to an output array
        
        nums.sort()
        output = set()


        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    output.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1

        return list(output)

