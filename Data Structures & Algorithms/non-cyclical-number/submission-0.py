class Solution:
    def isHappy(self, n: int) -> bool:
        def nxt(n):
            total = 0

            for ch in str(n):
                total += int(ch) ** 2
                
            return total

        slow = fast = n
        while True:
            slow = nxt(slow)
            fast = nxt(nxt(fast))
            if slow == fast:
                return slow == 1