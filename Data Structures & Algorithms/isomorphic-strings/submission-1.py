class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        myDict = {}
        mappings = set()
        result = True

        for i in range(len(s)):
            if s[i] in myDict:
                # Check to see if the value of key s[i] == t[i]
                # if yes, continue, if not, we make result False and break out of loop
                if myDict[s[i]] == t[i]:
                    continue
                else:
                    result = False
                    break
            else:
                if t[i] in mappings:
                    result = False
                    break

                # Add s[i] as key to dict and map it to t[i]
                myDict[s[i]] = t[i]
                mappings.add(t[i])

        return result
