from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Handle an empty list explicitly
        if not strs:
            return "EMPTY_LIST"  # Special marker for an empty list
        
        # Concatenate strings with a delimiter
        res = ""
        for word in strs:
            res += "+" + word
        
        return res[1:]  # Remove the leading '+'

    def decode(self, s: str) -> List[str]:
        # Handle special marker for an empty list
        if s == "EMPTY_LIST":
            return []
        
        res = []
        word = ""
        
        # Split the encoded string back into components
        for letter in s:
            if letter == "+":
                res.append(word)
                word = ""
            else:
                word += letter
        
        res.append(word)  # Add the last word
        return res
