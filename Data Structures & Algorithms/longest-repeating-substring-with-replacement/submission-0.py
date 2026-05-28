class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = 0
        map = {}
        l = 0
        r = 0

        while r < len(s):
            r += 1
            map = Counter(s[l:r])
            numLetterToChange = (r - l) - map.most_common(1)[0][1]
            if numLetterToChange > k:
                l += 1
            else:
                count = max(count, r-l)
            print(map)
            
        return count