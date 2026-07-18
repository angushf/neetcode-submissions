# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # will traverse the tree using a preorder traversal
        # every node will be added to a max heap of size k while the heap size is < k
        # if max heap is full we only replace a node if it's smaller than heap[0]

        maxHeap = []

        def dfs(node):
            nonlocal maxHeap
            if not node:
                return 

            heapq.heappush(maxHeap, -node.val)

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return -maxHeap[0]