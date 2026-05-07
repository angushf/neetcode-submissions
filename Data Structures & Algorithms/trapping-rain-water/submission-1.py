class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = [0] * len(height)
        maxRight = [0] * len(height)
        minLandR = [0] * len(height)
        result = 0

        maxLeftSoFar = 0
        for i in range(len(height)):
            if i == 0:
                maxLeft[i] = 0
            else:
                maxLeft[i] = maxLeftSoFar
            maxLeftSoFar = max(maxLeftSoFar, height[i])

        maxRightSoFar = 0
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                maxRight[i] = 0
            else:
                maxRight[i] = maxRightSoFar
            maxRightSoFar = max(maxRightSoFar, height[i])

        for i in range(len(height)):
            minLandR[i] = min(maxLeft[i], maxRight[i])

        for i in range(len(height)):
            answer = (minLandR[i] - height[i])
            if answer < 0:
                answer = 0
            result += answer
        
        return result