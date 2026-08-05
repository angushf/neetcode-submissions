import math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)

        for _ in range(k):
            max_pile = -heapq.heappop(max_heap)
            new_pile = math.floor(math.sqrt(max_pile))

            heapq.heappush(max_heap, -new_pile)

        return abs(sum(max_heap))