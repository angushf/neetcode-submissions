class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Fixed (?)
        # valid() - do the char -> counts maps equal each other
        # return True if yes

        count = Counter(s1)

        left = 0    
        right = len(s1)

        while right <= len(s2):
            val = Counter(s2[left:right])
            if val == count:
                return True

            right += 1
            left += 1

        return False

            
        