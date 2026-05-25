class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)

        a1 = 0
        a2 = float("inf")

        for val in freq.values():
            if val % 2 != 0 and val > a1:
                a1 = val
            
            if val % 2 == 0 and val < a2:
                a2 = val

        return a1 - a2
