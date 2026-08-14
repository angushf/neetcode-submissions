"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return node
        
        # maps old_node -> new_node
        old_to_new = {node: Node(node.val)}

        q = deque([node])

        while q:
            curr = q.popleft()

            if curr not in old_to_new:
                old_to_new[curr] = Node(curr.val)

            for neighbour in curr.neighbors:
                if neighbour not in old_to_new:
                    old_to_new[neighbour] = Node(neighbour.val)
                    q.append(neighbour)

                old_to_new[curr].neighbors.append(old_to_new[neighbour])



        return old_to_new[node]