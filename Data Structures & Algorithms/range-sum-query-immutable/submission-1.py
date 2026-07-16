class NumArray:

    def __init__(self, nums: List[int]):
        self.p = [0] * (len(nums) + 1)

        for i in range(1, len(self.p)):
            self.p[i] = self.p[i-1] + nums[i-1]


    def sumRange(self, left: int, right: int) -> int:
        return self.p[right+1] - self.p[left]
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
 
    #    nums = [1,2,3,4]
    #    p    = [0,1,3,6,10]

    #    sumRange(0, 3) = p[right+1] - p[left] = 10 - 0 = 10