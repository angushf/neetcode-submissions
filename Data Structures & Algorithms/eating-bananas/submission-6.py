class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)


        def feasible(speed):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / speed)

            return hours <= h


        while lo < hi:
            mid = (lo + hi) // 2

            if feasible(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
