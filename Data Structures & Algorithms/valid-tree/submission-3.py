class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Traverse graph using DFS or BFS traversal
        # For each node, check if it's in our seen_set
        # if it is, we have a cycle, if not, add to set and continue

        seen_set = set()
        result = True

        # map = {0: [1, 2, 3], 1: [0,4], 2: [0]}
        map = {}

        for edge in edges:
            node1, node2 = edge
            if node1 in map:
                map[node1] = map.get(node1, []) + [node2]
            else:
                map[node1] = [node2]

            if node2 in map:
                map[node2] = map.get(node2, []) + [node1]
            else:
                map[node2] = [node1]

        print(map)

        def dfs(node, prev):
            nonlocal result
            
            if node in seen_set:
                result = False
                return

            seen_set.add(node)

            for i in range(len(map.get(node, []))):
                if map[node][i] == prev:
                    continue
                dfs(map[node][i], node) 

        dfs(0, -1)

        return result and len(seen_set) == n


