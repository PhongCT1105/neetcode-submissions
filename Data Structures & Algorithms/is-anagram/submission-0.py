class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_count, t_count = [0] * 26, [0] * 26

        for c in s:
            s_count[ord(c) - ord('a')] += 1
        for c in t:
            t_count[ord(c) - ord('a')] += 1

        return s_count == t_count