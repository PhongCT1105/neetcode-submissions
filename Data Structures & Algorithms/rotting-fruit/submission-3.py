class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        res = -1
        # BFS
        # Step 1: Collect all the rotten fruit for the starting point
        rotten_fruits = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_fruits.append((r,c))
        if not rotten_fruits:
            return 0
        # Step 2: BFS of the rotten fruit and count the time when no way to go more

        # Helper function to check if the fruit is in bound and fresh:
        def convert_fresh(r,c):
            if not(0 <= r < ROWS) or not(0 <= c < COLS):
                return False #(Out bound)
            if grid[r][c] != 1:
                return False #(Rotten and empty cell)
            # Convert fresh fruit into rotten fruit
            grid[r][c] = 2
            q.append((r,c))

        from collections import deque
        q = deque(rotten_fruits)
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                convert_fresh(r+1,c)
                convert_fresh(r-1,c)
                convert_fresh(r,c+1)
                convert_fresh(r,c-1)
            res += 1

        # Step 3: Traverse through everything to check if any fresh fruit left
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return res