class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: 
            return [[1]]
        
        if numRows == 2:
            return [[1], [1,1]]

        result = [[1], [1,1]]

        for i in range(1, numRows-1):
            index = 1
            newLevel = [1]
            while index < len(result[i]):
                newLevel.append(result[i][index] + result[i][index-1])
                index += 1
            newLevel.append(1)
            result.append(newLevel)

        return result

