class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcTotalHoursSpent(speed):
            hours = 0

            for pile in piles:
                hours += math.ceil((pile / speed))
            
            return hours


        minSpeed = 1
        maxSpeed = max(piles)
        result = maxSpeed
        if minSpeed > maxSpeed and calcTotalHoursSpent(minSpeed) <= h:
            result = minSpeed



        def binarySearch(lowerBound, upperBound):
            if lowerBound > upperBound:
                return

            mid = (lowerBound + upperBound) // 2

            hours = calcTotalHoursSpent(mid)
            nonlocal result
            if hours <= h:
                result = mid
                binarySearch(lowerBound, mid-1)
            else:
                binarySearch(mid+1, upperBound)

            

        binarySearch(minSpeed, maxSpeed)
        return result
