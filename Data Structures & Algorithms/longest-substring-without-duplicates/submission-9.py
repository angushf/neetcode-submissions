class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        map = {}

        l = 0

        for r, ch in enumerate(s):
            # ADD
            map[ch] = map.get(ch, 0) + 1

            # SHRINK
            while map[ch] > 1:
                map[s[l]] -= 1
                if map[s[l]] == 0:
                    del map[s[l]]
                l += 1

            result = max(result, r-l+1)

        return result