class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Variable window
        # Add letter to windowCount
        # Condition: Shrink while current letter has a count > 1
        # Record R - L + 1


        count = Counter()
        result = 0

        l = 0

        for r, ch in enumerate(s):
            # ADD
            count[ch] = count.get(ch, 0) + 1

            # SHRINK
            while count[ch] > 1:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1

            # RECORD
            result = max(result, r-l+1)

        return result
