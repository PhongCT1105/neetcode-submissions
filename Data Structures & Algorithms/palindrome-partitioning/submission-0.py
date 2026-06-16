class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            # If i reaches the end, we made a full valid partition
            if i == len(s):
                res.append(part.copy())
                return

            # Try every possible cut starting from index i
            for j in range(i, len(s)):
                print(j, i)
                if isPali(i, j):
                    part.append(s[i:j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res