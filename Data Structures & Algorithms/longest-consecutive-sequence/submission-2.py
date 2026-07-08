class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row_set = [set() for _ in range(n)]
        col_set = [set() for _ in range(n)]
        sqr_set = [set() for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if board[r][c] == '.':
                    continue
                box = (r // 3) * 3 + (c // 3)
                if (board[r][c] in row_set[r]) or (board[r][c] in col_set[c]) or (board[r][c] in sqr_set[box]):
                    return False
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                sqr_set[box].add(board[r][c])

        return True