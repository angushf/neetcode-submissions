class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [-num for num in nums]
        self.k = k
        heapq.heapify(self.heap)
        print(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        return -heapq.nsmallest(self.k, self.heap)[-1]
