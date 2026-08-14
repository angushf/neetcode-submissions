class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF # mask

        carry = ((a & b) << 1) & MASK
        result = (a ^ b) & MASK
        while carry:
            tmp = carry
            carry = ((carry & result) << 1) & MASK
            result = (result ^ tmp) & MASK
        

        return ~(result ^ MASK) if result > 0x7FFFFFFF else result