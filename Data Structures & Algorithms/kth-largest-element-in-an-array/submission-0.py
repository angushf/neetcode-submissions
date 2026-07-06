import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [0] * (len(nums))
        
        for i, num in enumerate(nums):
            heap[i] = -num

        heapq.heapify(heap)

        result = 0

        while k > 0:
            result = -heapq.heappop(heap)
            k -= 1

        return result