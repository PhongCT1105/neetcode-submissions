class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str = ""
        for word in strs:
            encode_str += f"{len(word)}#{word}"
        return encode_str

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            length = 0
            while ord('0') <= ord(s[i]) <= ord('9'):
                length *= 10
                length += int(s[i])
                i += 1
            res.append(s[i+1: i+length+1])
            i = i + length + 1

        return res