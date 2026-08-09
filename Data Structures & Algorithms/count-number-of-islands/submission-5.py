class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # iterate through 2D grid and start a DFS search when an element == "1"
        # increment result by 1 after we finish each DFS
        # turn every 1 into "0" during dfs
        # return result after iterating through grid

        result = 0
        visited = set()

        def dfs(row, col, visited):
            if row < 0 or row > len(grid)-1:
                return

            if col < 0 or col > len(grid[0])-1:
                return

            if grid[row][col] == "0":
                return

            if (row, col) in visited:
                return

            visited.add((row, col))

            dfs(row-1, col, visited)
            dfs(row+1, col, visited)
            dfs(row, col+1, visited)
            dfs(row, col-1, visited)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r, c, visited)
                    result += 1

        return result
