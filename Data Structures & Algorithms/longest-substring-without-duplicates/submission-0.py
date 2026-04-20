class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        s = list(s)
        res = 0
        ptr = 0
        visited = set()
        for i in range(len(s)):
            while s[i] in visited:
                visited.remove(s[ptr])
                ptr += 1

            visited.add(s[i])
            res = max(res, i-ptr+1)
        
        return res