class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_char(c):
            if ord('a') <= ord(c) <= ord('z'):
                return True
            if ord('A') <= ord(c) <= ord('Z'):
                return True
            if ord('0') <= ord(c) <= ord('9'):
                return True
            return False

        l, r = 0, len(s)-1
        while l <= r:
            print(s[l], s[r])
            if not is_char(s[l]):
                l += 1
                continue
            if not is_char(s[r]):
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1  
            r -= 1
        return True
