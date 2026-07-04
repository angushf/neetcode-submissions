class NumArray:

    def __init__(self, nums: List[int]):
        self.p = [0] * (len(nums) + 1)

        for i, num in enumerate(nums):
            self.p[i+1] = self.p[i] + num

    def sumRange(self, left: int, right: int) -> int:
        result = self.p[right + 1] - self.p[left]

        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)