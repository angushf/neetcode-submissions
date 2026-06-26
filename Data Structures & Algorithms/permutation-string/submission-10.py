class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed window
        # Condition is does the window count == s1 count
        # Add R pointer to window count and decrement l pointer from window count

        count = Counter(s1)

        windowCount = Counter(s2[0:len(s1)])

        if windowCount == count:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            # add
            windowCount[s2[r]] = windowCount.get(s2[r], 0) + 1

            # shrink
            windowCount[s2[l]] -= 1
            if windowCount[s2[l]] == 0:
                del windowCount[s2[l]]
            l += 1

            # condition
            if windowCount == count:
                return True

        return False