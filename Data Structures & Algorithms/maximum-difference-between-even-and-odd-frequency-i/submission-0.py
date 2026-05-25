class Solution:
    def maxDifference(self, s: str) -> int:
        mySet = set(s)
        map = {}

        for letter in mySet:
            map[letter] = s.count(letter)

        a1 = 0
        a2 = float("inf")
        
        for val in map.values():
            if val % 2 != 0 and val > a1:
                a1 = val
            
            if val % 2 == 0 and val < a2:
                a2 = val

        return a1 - a2
