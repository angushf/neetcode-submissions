class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Converging pointers L and R
        # Condition is to check whether numbers[l] + numbers[r] == target
        # If so, return [numbers[l], numbers[r]]

        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

