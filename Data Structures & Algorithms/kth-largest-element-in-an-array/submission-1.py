import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [0] * (len(nums))
        
        for i, num in enumerate(nums):
            heap[i] = -num

        heapq.heapify(heap)

        return -heapq.nsmallest(k, heap)[-1]