class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        myMap = {}
        s_arr = s.split()       
        seenWords = set() 

        if len(pattern) != len(s_arr):
                return False

        for idx, letter in enumerate(pattern):
                if letter in myMap:
                        if myMap[letter] != s_arr[idx]:
                                return False
                if s_arr[idx] in seenWords and letter not in myMap:
                        return False

                seenWords.add(s_arr[idx])

                myMap[letter] = s_arr[idx]

        return True

                
        