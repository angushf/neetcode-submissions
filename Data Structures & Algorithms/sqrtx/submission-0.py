class Solution:
    def mySqrt(self, x: int) -> int:
        num = 1
        
        while (num * num) <= x:
            if (num * num) == x:
                return num

            num = num + 1

        return num - 1

    
    