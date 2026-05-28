class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = 0
        count = {}
        s1Count = Counter(s1)
        result = False

        while l + len(s1) <= len(s2):
            while r < len(s1) + l:
                count[s2[r]] = count.get(s2[r], 0) + 1
                r += 1

            result = count == s1Count
            if result == True:
                break

            count = {}
            l += 1
            r = l






        return result