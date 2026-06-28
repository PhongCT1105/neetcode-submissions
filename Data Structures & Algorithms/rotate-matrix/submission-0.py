class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        
        ROWS, COLS = len(matrix), len(matrix[0])
        res = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                new_row = c
                new_col = ROWS - 1 - r
                res[new_row][new_col] = matrix[r][c]

        # Copy back into matrix because LeetCode wants in-place modification
        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] = res[r][c]