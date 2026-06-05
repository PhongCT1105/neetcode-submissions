class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        r, c = 0, 0
        ptr = 0
        ROWS, COLS = len(board), len(board[0])
        res = False
        visited = set()

        def dfs(r, c, ptr):
            # Edge case: Outside of the grid return:
            if not 0 <= r < ROWS:
                return
            if not 0 <= c < COLS:
                return
            # Edge case: If visited return:
            if (r,c) in visited:
                return
            # Edge case: Not match:
            if board[r][c] != word[ptr]:
                return

            # Base case: return true if all word are match:
            if ptr == len(word) - 1:
                nonlocal res
                res = True
                return 

            ptr += 1
            visited.add((r,c))
            # Explore neighbors:
            dfs(r-1, c, ptr)
            dfs(r+1, c, ptr)
            dfs(r, c+1, ptr)
            dfs(r, c-1, ptr)

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, ptr)

        return res