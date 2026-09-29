class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        l = 0 
        seen = set([s[l]])
        res = 1
        cnt = 1
        for r in range(1,len(s)):
            if s[r] not in seen:
                seen.add(s[r])
                cnt += 1
                res = max(res, cnt)
            else:
                while s[r] in seen:
                    seen.discard(s[l])
                    l += 1
                cnt = 0

        return max(res, cnt)