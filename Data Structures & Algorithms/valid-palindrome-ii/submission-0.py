class Solution:
    def validPalindrome(self, s: str) -> bool:
        result = False

        for i in range(len(s)):
            arr = list(s)
            arr.pop(i)
            if arr == arr[::-1]:
                result = True
                break

        return result