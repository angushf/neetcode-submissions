class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0

        for i in range(len(details)):
            age = int(details[i][11:13])
            if age > 60:
                result += 1

        return result