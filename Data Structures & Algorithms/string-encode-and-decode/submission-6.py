class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + "+" + word
    
        return (res - res[0])

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