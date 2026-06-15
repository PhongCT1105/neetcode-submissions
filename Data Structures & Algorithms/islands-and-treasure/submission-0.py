class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        from collections import deque
        # Using bfs and traverse from every reward to all reachable land
        q = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))

        visited = set()
        
        def add_node(r,c):
            if not(0 <= r < ROWS and 0 <= c < COLS):
                return
            if grid[r][c] == -1:
                return
            if (r,c) in visited:
                return
            if grid[r][c] == INF:
                grid[r][c] = dist
            q.append((r,c))
            visited.add((r,c))
        dist = 1
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                # Traverse through all the land = INF
                # Add the new in if is INF else skip
                # Since we use BFS, the lowest distance is always distance
                add_node(r+1,c)
                add_node(r-1,c)
                add_node(r,c+1)
                add_node(r,c-1)
            dist += 1

        