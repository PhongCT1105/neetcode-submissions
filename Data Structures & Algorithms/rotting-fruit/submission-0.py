class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Check if rotten fruit first:
        # How many rotten fruit range: Is there only 1 or many in what range
        # => Could be many

        if not grid or not grid[0]:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        # Phase 1: Detect all the position of the rotten fruit
        rotten_fruit = []
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten_fruit.append((r, c))

        # Phase 2: Expand by BFS to make all the fruit in the range rotten and get the time
        time = 0
        def is_valid (r, c):
            if r >= 0 and r <= ROWS-1 and c >= 0 and c <= COLS-1:
                if grid[r][c] == 1:
                    return True
                else:
                    return False
            else:
                return False
        while rotten_fruit:
            changed = False            
            for i in range(len(rotten_fruit)):
                fruit = rotten_fruit.pop(0)
                r, c = fruit[0], fruit[1]
                if is_valid(r-1, c):
                    grid[r-1][c] = 2
                    rotten_fruit.append((r-1,c))
                    changed = True
                if is_valid(r+1, c):
                    grid[r+1][c] = 2
                    rotten_fruit.append((r+1,c))
                    changed = True
                if is_valid(r, c-1):
                    grid[r][c-1] = 2
                    rotten_fruit.append((r,c-1))
                    changed = True
                if is_valid(r, c+1):
                    grid[r][c+1] = 2
                    rotten_fruit.append((r,c+1))
                    changed = True
            if changed == True:
                time += 1
        # Phase 3: Check if any fruit is good if not return time else return -1
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        else:
            return time