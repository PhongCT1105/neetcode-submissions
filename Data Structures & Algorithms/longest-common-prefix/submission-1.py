class Tries:
    def __init__(self):
        self.child = {}
        self.cnt = 0

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Tries()
        if not strs:
            return ""
        for word in strs:
            curr = root
            for c in word:
                if c not in curr.child:
                    curr.child[c] = Tries()

                curr = curr.child[c]
                curr.cnt += 1

        res = []
        curr = root
        n = len(strs)
        for c in strs[0]:
            if c in curr.child and curr.child[c].cnt == n:
                res.append(c)
                curr = curr.child[c]
            else:
                return "".join(res)
        
        return "".join(res)