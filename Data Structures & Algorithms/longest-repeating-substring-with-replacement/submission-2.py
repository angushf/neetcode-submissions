class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Variable window
        # valid(): len(window) - most_freq <= k
        # Update global variable via right - left + 1

        result = 0
        left = 0
        window = Counter()

        for right, ch in enumerate(s):
            # ADD
            window[ch] += 1

            # SHRINK
            while (right - left + 1) - window.most_common(1)[0][1] > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
                
            # RECORD
            result = max(result, right-left+1)

        return result