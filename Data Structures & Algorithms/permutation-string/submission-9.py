class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed window
        # Condition = counter of s1 == counter of window - add & subtract as window slides right
        # Return False if loop completes without returning True

        count = Counter(s1)
        windowCount = Counter(s2[0:len(s1)])

        if windowCount == count:
            return True
        

        for r in range(len(s1), len(s2)):
            # ADD
            windowCount[s2[r]] = windowCount.get(s2[r], 0) + 1
            windowCount[s2[r - len(s1)]] = windowCount.get(s2[r - len(s1)]) - 1
            if windowCount[s2[r - len(s1)]] == 0:
                del windowCount[s2[r - len(s1)]]

            # Condition
            if windowCount == count:
                return True

        return False
             


            
