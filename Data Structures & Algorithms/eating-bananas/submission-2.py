class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calcTotalHoursSpent(speed):
            hours = 0

            for pile in piles:
                hours += math.ceil((pile / speed))
            
            return hours


        minSpeed = (1, calcTotalHoursSpent(1))
        maxSpeed = (max(piles), calcTotalHoursSpent(max(piles)))
        result = maxSpeed
        if minSpeed[1] > maxSpeed[1] and minSpeed[1] <= h:
            result = minSpeed



        def binarySearch(lowerBound, upperBound):
            if lowerBound > upperBound:
                return

            mid = (lowerBound + upperBound) // 2

            hours = calcTotalHoursSpent(mid)
            nonlocal result
            if hours <= h:
                result = (mid, hours)
                binarySearch(lowerBound, mid-1)
            else:
                binarySearch(mid+1, upperBound)

            

        binarySearch(minSpeed[0], maxSpeed[0])
        return result[0]
