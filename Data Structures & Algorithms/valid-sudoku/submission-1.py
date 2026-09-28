class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False

        rows_set = [set() for i in range(9)]
        cols_set = [set() for i in range(9)]
        grid_set = [set() for i in range(9)]
        
        for r in range(9):
            for c in range(9):
                # Access to each element in board[r][c]
                # Check in rows set
                if board[r][c] == '.':
                    continue
                if board[r][c] in rows_set[r]:
                    return False
                else:
                    rows_set[r].add(board[r][c])
                # Check in cols set
                if board[r][c] in cols_set[c]:
                    return False
                else:
                    cols_set[c].add(board[r][c])
                # Check in grid set
                index = (r//3)*3 + (c//3)
                if board[r][c] in grid_set[index]:
                    return False
                else:
                    grid_set[index].add(board[r][c])
        return True