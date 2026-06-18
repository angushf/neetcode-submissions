class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Converging pointers cuz sorted array and we can discard left/right half
        # condition is numbers[l] + numbers[r] == target
        # Return [l+1,r+1] as soon as we can

        l = 0
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l+1, r+1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1

            