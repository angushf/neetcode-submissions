class Solution:
    def isHappy(self, n: int) -> bool:
        def nxt(n):
            result = 0
            for ch in str(n):
                result += int(ch) ** 2
            return result

        slow = fast = n
        while True:
            slow = nxt(slow)
            fast = nxt(nxt(fast))

            if slow == fast:
                return slow == 1

        
