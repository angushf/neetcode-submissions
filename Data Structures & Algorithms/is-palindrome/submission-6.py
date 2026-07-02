class Solution:
    def isPalindrome(self, s: str) -> bool:
        # converging pointers - start at s[0] and s[-1]
        # while either pointer is not alphanumeric, increment/decrement pointer appropriately
        # condition: return False if s[l].lower() != s[r].lower(). If pointers converge, and loop
        # finishes, return True

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True