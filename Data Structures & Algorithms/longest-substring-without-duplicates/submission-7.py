class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Variable window
        # Condition is keep on adding a character to count map until we hit first duplicate
        # then, shrink window by decrementing s[l] from count map and incrementing l
        # Add max length to a global variable
        count = Counter()

        l = 0
        result = 0

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
            result = max(result, r - l + 1)

        return result