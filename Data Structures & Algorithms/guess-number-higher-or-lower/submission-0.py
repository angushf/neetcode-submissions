# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lowerBound = None
        upperBound = None

        num = n
        guesss = guess(num)

        while guesss != 0:
            if guesss == -1:
                # guess > pick
                upperBound = num
            else:
                # guess < pick
                lowerBound = num

            if upperBound == None:
                num = lowerBound * 2
                guesss = guess(num)
            elif lowerBound == None:
                num = upperBound // 2
                guesss = guess(num)
            else:
                num = (lowerBound + upperBound) // 2
                guesss = guess(num)

        return num

        
        