class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        index = 0

        for i in range(len(t)):
            if index < len(s) and t[i] == s[index]:
                index = index + 1
            
        return index == len(s)