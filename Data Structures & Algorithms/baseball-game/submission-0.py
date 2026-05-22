class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for operation in operations:
            if operation == "+":
                num1 = stack[-1]
                num2 = stack[-2]
                result = num1 + num2

                stack.append(result)
            elif operation == "C":
                stack.pop(-1)
            elif operation == "D":
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(operation))
            

        return sum(stack)