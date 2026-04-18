from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Use length-based encoding
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            # Find the next delimiter '#'
            j = s.find('#', i)
            # Extract the length of the word before the delimiter
            length = int(s[i:j])
            # Extract the word using the specified length
            word = s[j + 1: j + 1 + length]
            res.append(word)
            # Move the pointer to the next word
            i = j + 1 + length

        return res
