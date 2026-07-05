class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = Counter(s1)
        win_count = Counter(s2[0:len(s1)])


        if s1_count == win_count:
            return True

        for r in range(len(s1), len(s2)):   
            win_count[s2[r]] = win_count.get(s2[r], 0) + 1

            win_count[s2[r - len(s1)]] -= 1
            if win_count[s2[r - len(s1)]] == 0:
                del win_count[s2[r - len(s1)]]

            if s1_count == win_count:
                return True

        return False