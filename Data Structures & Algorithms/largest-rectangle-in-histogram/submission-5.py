class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0

        for index, height in enumerate(heights):
            start = index

            while stack and height < stack[-1][1]:
                i, h = stack.pop(-1)
                area = max(area, (index - i) * h)
                #potentially reassign index here
                start = i

            stack.append((start, height))

        for item in stack:
            area = max(area, item[1] * (len(heights) - item[0]))

        return area