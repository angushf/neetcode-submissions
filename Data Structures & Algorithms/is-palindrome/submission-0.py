class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = "".join(char for char in s if char.isalnum()).lower()

        leftPtr =  0
        rightPtr = len(cleanString) - 1

        while leftPtr < rightPtr:
            if cleanString[leftPtr] != cleanString[rightPtr]:
                print
                return False
            leftPtr  += 1
            rightPtr -= 1

        return True