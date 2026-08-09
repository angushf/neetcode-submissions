class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0

        visited = set()
        stack = []

        def iterative_dfs():
            while stack:
                r, c = stack.pop()
                
                for i in ((r-1, c), (r+1, c), (r,c+1), (r,c-1)):
                    nr, nc = i

                    if 0 <= nr < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1" and (nr, nc) not in visited:
                        stack.append((nr, nc))
                        visited.add((nr, nc))






        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    stack.append((r, c))
                    iterative_dfs()
                    result += 1

        return result