class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [-1] * (n+1)

        def countOnes(bin_num):
            count = 0
            while bin_num:
                bin_num &= (bin_num-1)
                count += 1
            result[i] = count


        
        for i in range(n+1):
            countOnes(i)

        return result
        