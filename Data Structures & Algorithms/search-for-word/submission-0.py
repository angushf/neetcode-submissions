class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def dfs(row, col, wordIdx):
            # valid path
            if wordIdx == len(word):
                return True

            # invalid path(s)
            if row < 0 or row >= len(board):
                return False

            if col < 0 or col >= len(board[0]):
                return False

            if (row, col) in visited:
                return False

            if board[row][col] != word[wordIdx]:
                return False

            # increment wordIdx by one, add letter to visited
            # and call 4 recursive functions
            visited.add((row, col))
            found = (dfs(row - 1, col, wordIdx + 1) or  # top
                   dfs(row, col - 1, wordIdx + 1) or  # left
                   dfs(row, col + 1, wordIdx + 1) or  # right
                   dfs(row + 1, col, wordIdx + 1))     # bottom
            visited.remove((row, col))

            return found

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col, 0):
                    return True

        return False
            
