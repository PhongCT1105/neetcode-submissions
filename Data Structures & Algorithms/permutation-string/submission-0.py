class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        from collections import Counter
        s1_counter = Counter(s1)

        l, r = 0, len(s1) - 1        
        while r < len(s2):
            s2_counter = Counter(s2[l:r+1])
            if s1_counter == s2_counter:
                return True
            l += 1
            r += 1

        return False

                