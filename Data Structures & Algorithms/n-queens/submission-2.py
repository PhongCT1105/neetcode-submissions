class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]

        visited_c = set()
        visited_d1 = set()  
        visited_d2 = set()
        res = []
        queens = []
        def backtrack(r, c):
            if not (0 <= r < n):
                return
            if not (0 <= c < n):
                return
            if c in visited_c:
                return
            if (r - c) in visited_d1:
                return
            if (r + c) in visited_d2:
                return

            queens.append((r, c))
            visited_c.add(c)
            visited_d1.add(r - c)
            visited_d2.add(r + c)

            if len(queens) == n:
                res.append(queens[:])
            else:
                for next_c in range(n):
                    backtrack(r + 1, next_c)

            queens.pop()
            visited_c.remove(c)
            visited_d1.remove(r - c)
            visited_d2.remove(r + c)
        for c in range(n):
            backtrack(0,c)
        final_res = []
        for i in range(len(res)):
            mp = [['.'] * n for _ in range(n)]
            for r,c in res[i]:
                mp[r][c] = 'Q'
            for r in range(n):
                mp[r] = ''.join(mp[r])
            final_res.append(mp)

        return final_res