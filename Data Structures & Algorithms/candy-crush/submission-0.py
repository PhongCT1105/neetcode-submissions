class Solution:        
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        
        ROWS, COLS = len(board), len(board[0])
        
        def find():
            crush_set = set()
            # Check horizontal
            for row in range(ROWS):
                for col in range(1, COLS-1):
                    if board[row][col] == board[row][col-1] and board[row][col] == board[row][col+1] and board[row][col] != 0:
                        crush_set.add((row, col))
                        crush_set.add((row,col-1))
                        crush_set.add((row,col+1))

            # Check vertical
            for col in range(COLS):
                for row in range(1, ROWS-1):
                    if board[row][col] == board[row-1][col] and board[row][col] == board[row+1][col] and board[row][col] != 0:
                        crush_set.add((row,col))
                        crush_set.add((row-1,col))
                        crush_set.add((row+1,col))
            
            return crush_set

        def debug_find():
            crush_set = find()
            for i in crush_set:
                row, col = i[0], i[1]
                print("Location of (", row, " ", col, "): ", board[row][col])

        def crush(crush_set):
            for i in crush_set:
                row, col = i[0], i[1]
                board[row][col] = 0

        def drop():
            for col in range(COLS):
                blank = ROWS - 1
                for row in range(ROWS - 1, -1, -1):
                    if board[row][col] != 0:
                        board[blank][col] = board[row][col]
                        blank -= 1

                for row in range(blank, -1, -1):
                    board[row][col] = 0

        crush_set = find()
        while crush_set:
            crush(crush_set)
            drop()
            print(board)
            crush_set = find()
        
        return board
