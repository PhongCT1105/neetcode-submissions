class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Store the counter of t
        counter = {}
        for c in t:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        l = 0

        def isValid(l, r):
            tmp_counter = counter.copy()
            for i in range(l, r+1):
                if s[i] in tmp_counter:
                    tmp_counter[s[i]] -= 1
            return max(tmp_counter.values()) <= 0
        
        res = None

        for r in range(len(s)):
            while isValid(l, r):
                if res is None or (r-l+1)<(res[1]-res[0]+1):
                    res = (l, r)
                l += 1
            
        if res is None:
            return ""
            
        return s[res[0]:res[1]+1]

        