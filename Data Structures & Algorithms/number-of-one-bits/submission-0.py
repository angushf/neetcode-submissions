class Solution:
    def hammingWeight(self, n: int) -> int:
        result = 0

        while n != 0:
            val = n % 2
            if val != 0 :
                result += 1
            n = n >> 1

        return result