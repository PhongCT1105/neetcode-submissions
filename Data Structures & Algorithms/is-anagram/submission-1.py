class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def return_map(s):
            arr = [0] * 26
            for c in s:
                arr[ord(c)-ord('a')] += 1
            return arr
        
        return return_map(s) == return_map(t)