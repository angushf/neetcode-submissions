class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            val = n & 1
            res = res | val
            n = n >> 1
            if i != 31:
                res = res << 1

        print(bin(res))
        return res
            