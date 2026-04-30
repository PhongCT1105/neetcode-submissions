class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visit = set()

        def dfs(r, c):
            if (r,c) in visit:
                return 
            if r < 0 or c < 0 or r > ROWS - 1 or c > COLS - 1 or grid[r][c] == 0:
                nonlocal res
                res += 1
                return
            
            visit.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(ROWS):
            for c in range(COLS):
                # Detect island first:
                if grid[r][c] == 1:
                    dfs(r, c)
                    break

        return res