class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # BS on the answer range
        # Predicate is feasible(k) <= h
        # Find the first T in the FFF..TTTT monotinc relationship between [1, max(piles)]

        def is_feasible(k):
            return sum(math.ceil(pile / k) for pile in piles) <= h

        lo = 1
        hi = max(piles)

        while lo < hi:
            mid = (lo + hi) // 2

            if is_feasible(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo



