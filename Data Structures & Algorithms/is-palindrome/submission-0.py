class Solution:

    def is_char(self, c):
        if ord('z') >= ord(c) and ord('a') <= ord(c):
            return True
        elif ord('Z') >= ord(c) and ord('A') <= ord(c):
            return True
        elif ord('9') >= ord(c) and ord('0') <= ord(c):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if self.is_char(s[l]) == False:
                l += 1
                continue
            if self.is_char(s[r]) == False:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
    
        return True