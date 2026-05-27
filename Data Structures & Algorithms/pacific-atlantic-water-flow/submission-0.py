class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(heights), len(heights[0])

        def is_valid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def can_go(r1, c1, r2, c2):
            return heights[r1][c1] >= heights[r2][c2]

        from collections import deque
        res = []

        for start_r in range(ROWS):
            for start_c in range(COLS):
                q = deque([(start_r, start_c)])
                visited = set([(start_r, start_c)])

                has_pacific, has_atlantic = False, False

                while q:
                    r, c = q.popleft()

                    if r == 0 or c == 0:
                        has_pacific = True

                    if r == ROWS - 1 or c == COLS - 1:
                        has_atlantic = True

                    for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                        if is_valid(nr, nc) and (nr, nc) not in visited:
                            if can_go(r, c, nr, nc):
                                visited.add((nr, nc))
                                q.append((nr, nc))

                if has_pacific and has_atlantic:
                    res.append([start_r, start_c])

        return res