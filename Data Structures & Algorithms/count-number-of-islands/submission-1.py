class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        visited = set()

        def dfs(r,c):
            # If out of bound:
            if not(0 <= r < ROWS) or not(0 <= c < COLS):
                return 
            # If water skip:
            if grid[r][c] == "0":
                return
            # If already visited skip:
            if (r,c) in visited:
                return
            grid[r][c] = "0"
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,r)
            dfs(r,c+1)
            dfs(r,c-1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r,c)
                    res += 1

        return res