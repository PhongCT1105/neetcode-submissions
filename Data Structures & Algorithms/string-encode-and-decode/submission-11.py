class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res = res + "+" + word

        return res

    def decode(self, s: str) -> List[str]:
        res = []
        word = ""

        if str[0] == "+":
            str = str[1:]

        for letter in s:
            if letter == "+":
                res.append(word)
                word = ""
            else:
                word = word + letter

        res.append(word)
        return res