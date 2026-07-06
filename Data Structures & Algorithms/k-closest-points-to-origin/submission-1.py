class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculate(coord):
            x, y = coord

            return math.sqrt((x - 0) ** 2 + (y - 0) ** 2)

        return heapq.nsmallest(k, points, key=lambda t:calculate(t))