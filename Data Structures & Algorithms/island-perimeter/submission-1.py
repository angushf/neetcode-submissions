class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        count = 0
        seen = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            nonlocal count
            if (r,c) in seen:
                return

            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 0:
                count += 1
                return

            seen.add((r,c))
            grid[r][c] = 0

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)

        return count
