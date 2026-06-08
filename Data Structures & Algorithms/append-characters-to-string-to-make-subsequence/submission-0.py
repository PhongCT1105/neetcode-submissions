class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        str1, str2 = 0, 0
        
        while str1 < len(s) and str2 < len(t):
            if s[str1] == t[str2]:
                str2 += 1
            str1 += 1

        return len(t[str2:])