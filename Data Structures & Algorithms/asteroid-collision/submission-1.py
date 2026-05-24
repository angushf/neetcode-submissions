class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        index = 0

        while index < len(asteroids):
            while stack and index < len(asteroids) and (stack[-1] > 0 and asteroids[index] < 0):
                leftSize = abs(stack[-1])
                rightSize = abs(asteroids[index])
                result = leftSize - rightSize
                if result == 0:
                    stack.pop(-1)
                    index += 1
                    continue
                elif result < 0:
                    stack.pop(-1)
                else:
                    index += 1
                    continue

            if index < len(asteroids):
                stack.append(asteroids[index]) # Add to stack
            index += 1

        return stack