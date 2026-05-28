class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        result = 0
        l = 0
        r = 0

        def most_frequent(myMap):
            result = 0
            for value in myMap.values():
                result = max(result, value)
            return result

        while r < len(s):
            if s[r] not in count:
                count[s[r]] = 1
            else:
                count[s[r]] = count[s[r]] + 1

            windowLength = (r - l) + 1
            most_freq = most_frequent(count)
        
            changesRequired = windowLength - most_freq

            while changesRequired > k:
                count[s[l]] = count[s[l]] - 1
                l += 1
                changesRequired = (r-l+1) - most_frequent(count)

            result = max(result, r-l+1)

            r += 1

        return result