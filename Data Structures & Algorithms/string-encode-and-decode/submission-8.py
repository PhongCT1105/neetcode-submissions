class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + "+" + word
    
        res = res[1:]
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""
        for letter in s:
            if letter == "+":
                res.append(word)
                word = ""
            else:
                word = word + letter

        res.append(word)
        return res