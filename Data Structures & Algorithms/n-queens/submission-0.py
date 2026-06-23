class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]

        visited_r = set()
        visited_c = set()
        visited_d1 = set()  
        visited_d2 = set()
        res = []
        queens = []

        def backtrack(r,c):
            if len(queens) == n:
                res.append(queens[:])
                return 
            if not (0 <= r < n):
                return
            if not (0 <= c < n):
                return
            if r in visited_r:
                return
            if c in visited_c:
                return
            if (r - c) in visited_d1:
                return
            if (r + c) in visited_d2:
                return

            queens.append((r,c))
            visited_r.add(r)
            visited_c.add(c)
            visited_d1.add(r - c)
            visited_d2.add(r + c)

            backtrack(r+1,c-1)
            backtrack(r-1,c+1)

            queens.pop()
            visited_r.remove(r)
            visited_c.remove(c)
            visited_d1.remove(r - c)
            visited_d2.remove(r + c)
        
        for r in range(n):
            for c in range(n):
                backtrack(r,c)
        final_res = []
        for i in range(len(res)):
            mp = [['.'] * n for _ in range(n)]
            for r,c in res[i]:
                mp[r][c] = 'Q'
            for r in range(n):
                mp[r] = ''.join(mp[r])
            final_res.append(mp)

        return final_res