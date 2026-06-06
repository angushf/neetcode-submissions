class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # two pointers: l & r
        # increment r while hashmap doesn't include all of t's letters
        # increment l while hashmap includes all of t's letters
        # save s[l-1: r+1] to global result var if shorter than it
        
        l = 0
        r = 0

        tMap = Counter(t)
        sMap = {}
        result = None

        while r < len(s):
            sMap[s[r]] = sMap.get(s[r], 0) + 1
            
            if all(sMap.get(char, 0) >= count for char, count in tMap.items()):
                while all(sMap.get(char, 0) >= count for char, count in tMap.items()):
                    if sMap[s[l]] == 1:
                        sMap.pop(s[l])
                    else:
                        sMap[s[l]] = sMap.get(s[l]) - 1

                    l += 1
                if result == None:
                    result = s[l-1:r+1]
                else:
                    if len(s[l-1:r+1]) < len(result):
                        result = s[l-1:r+1]
                
            r += 1

        print(result)
        print(sMap)
        return result or ""


        