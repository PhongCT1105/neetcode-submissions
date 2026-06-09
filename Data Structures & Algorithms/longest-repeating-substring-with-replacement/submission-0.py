class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force:

        # Consider every substring => Check if valid 
        # Valid means => number of all array - max character <= k

        res = 0
        count = [0] * 26
        l = 0

        for r in range(len(s)):
            idx = ord(s[r]) - ord('A')
            count[idx] += 1
            while (r-l+1) - max(count) > k:
                l += 1
                idx = ord(s[l]) - ord('A')
                count[idx] -= 1
            
            res = max(res, (r-l+1))
        
        return res