from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Variable
        # valid() = all unique chars in window, need to keep track of
        # seen chars and can put them in a set
        # store result (right - left + 1) in global variable after shrinking

        count = Counter()
        result = 0
        left = 0

        for right, char in enumerate(s):
            # add
            count[char] += 1

            # shrink
            while count[char] > 1:
                count[s[left]] -= 1
                left += 1
            
            # record
            result = max(result, right-left+1)

        return result