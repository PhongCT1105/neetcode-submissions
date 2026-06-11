class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        for r in range(ROWS):
            if board[r][0] == 'O':
                visited.add((r,0))
            if board[r][COLS-1] == 'O':
                visited.add((r,COLS-1))
        for c in range(COLS):
            if board[0][c] == 'O':
                visited.add((0,c))
            if board[ROWS-1][c] == 'O':
                visited.add((ROWS-1,c))

        def add_node(r,c):
            if not (0 <= r < ROWS and 0 <= c < COLS):
                return
            if board[r][c] ==  'X':
                return
            if (r,c) in visited:
                return
            q.append((r,c))

        # Traverse through all the O on visited to add them to visited
        from collections import deque
        q = deque(visited)
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if board[r][c] == 'O':
                    visited.add((r,c))
                add_node(r+1,c)
                add_node(r-1,c)
                add_node(r,c+1)
                add_node(r,c-1)

        # Traverse everything and mark every O that is not in visted
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r,c) not in visited:
                    board[r][c] = 'X'