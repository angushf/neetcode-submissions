class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        length = len(grid)
        mySet = {x for x in range(1, (length*length) + 1)}
        ans = []

        for arr in grid:
            for num in arr:
                if num not in mySet:
                    ans.append(num)
                    continue
                
                mySet.remove(num)

        ans.append(list(mySet)[0])
        return ans