class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed (?)
        # valid() - do the char -> counts maps equal each other
        # return True if yes
        if len(s1) > len(s2):
            return False

        need = Counter(s1)
        window = Counter()
        k = len(s1)

        for right, ch in enumerate(s2):
            # add
            window[ch] += 1

            # shrink    
            if right >= k:
                drop = s2[right - k]
                window[drop] -= 1
                if window[drop] == 0:
                    del window[drop]
            
            # record
            if window == need:
                return True

        return False
            
        