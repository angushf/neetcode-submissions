class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        stack = []

        for log in logs:
            if len(stack) == 0 and log == "../":
                continue

            if log == "../":
                stack.pop(-1)
            elif log == "./":
                continue
            else:
                stack.append(log)

        return len(stack)

            

            

            