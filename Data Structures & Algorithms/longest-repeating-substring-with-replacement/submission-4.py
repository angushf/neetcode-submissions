class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Variable window
        # Condition - len(window) - count.most_common(1) > k
        # Record in global variable: R - L + 1

        count = Counter()
        result = 0

        l = 0

        for r, ch in enumerate(s):
            # ADD
            count[ch] = count.get(ch, 0) + 1

            # SHRINK
            while (r - l + 1) - count.most_common(1)[0][1] > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                
                l += 1


            # RECORD
            result = max(result, r - l + 1)

        return result
