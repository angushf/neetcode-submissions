class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ptr1 = 0
        ptr2 = 0

        while ptr1 < len(word) and ptr2 < len(abbr):
            if abbr[ptr2].isdigit():
                if abbr[ptr2] == "0":
                    return False

                num = ""
                while ptr2 < len(abbr) and abbr[ptr2].isdigit():
                    num += abbr[ptr2]
                    ptr2 += 1
                num = int(num)
                ptr1 += num
            else:
                if word[ptr1] != abbr[ptr2]:
                    return False

                ptr1 += 1
                ptr2 += 1

        if ptr1 == len(word) and ptr2 == len(abbr):
            return True
        else:
            return False
