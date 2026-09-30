class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r,c):
            # Check inbound first:
            if not(0 <= r < ROWS) or not(0 <= c < COLS):
                return
            # Check if land:
            if grid[r][c] != 1:
                return
            nonlocal cnt
            cnt += 1
            grid[r][c] = 0

            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(ROWS):
            for c in range(COLS):
                cnt = 0
                if grid[r][c] == 1:
                    dfs(r,c)
                res = max(res,cnt)
        return res