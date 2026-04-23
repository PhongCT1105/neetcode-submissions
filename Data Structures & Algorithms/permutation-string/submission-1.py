class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        from collections import defaultdict
        cnt_s1 = [0] * 26
        for c in s1:
            cnt_s1[ord(c) - ord('a')] += 1
        
        l, r = 0, len(s1) - 1 
        cnt_s2 = [0] * 26
        for c in s2[:r+1]:
            cnt_s2[ord(c) - ord('a')] += 1
        
        while r < len(s2) - 1:
            if cnt_s1 == cnt_s2:
                return True
            cnt_s2[ord(s2[l]) - ord('a')] -= 1
            l += 1
            r += 1
            cnt_s2[ord(s2[r]) - ord('a')] += 1
        
        return cnt_s1 == cnt_s2
                