class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = list(zip(position, speed))

        reversed_sorted_posAndSpeed = sorted(posAndSpeed, reverse=True)
        print(reversed_sorted_posAndSpeed)

        stack = []
        carFleetCount = 0

        for item in reversed_sorted_posAndSpeed:
            milesToGo = target - item[0]
            mph = item[1]
            hoursLeft = milesToGo / mph

            if stack and hoursLeft > stack[-1]:
                while stack:
                    stack.pop(-1)
                carFleetCount += 1
                stack.append(hoursLeft)

            if len(stack) == 0:
                stack.append(hoursLeft)

        if len(stack) > 0:
            return carFleetCount + 1
        else:
            return carFleetCount

            