class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        ptr1, ptr2 = 0, 0

        while ptr2 < len(t) and ptr1 < len(s):
            if s[ptr1] == t[ptr2]:
                ptr1 += 1
            ptr2 += 1
        return ptr1 == len(s)
