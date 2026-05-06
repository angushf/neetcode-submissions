class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for i in range(len(tokens)):
            if tokens[i] in operators:
                # do said operation
                rightNum = stack.pop()
                leftNum = stack.pop()
                operation = tokens[i]
                result = 0

                match operation:
                    case '+':
                        result = leftNum + rightNum
                    case '-':
                        result = leftNum - rightNum
                    case '*':
                        result = leftNum * rightNum
                    case '/':
                        result = int(leftNum / rightNum)
                
                stack.append(result)
            else:
                # add number to stack
                stack.append(int(tokens[i]))

        return stack[0]
