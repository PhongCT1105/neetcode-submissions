class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word = []

        for i in range(len(s)-1, -1, -1):

            if s[i] != " ":
                word.append(s[i])
            elif word and s[i] == " ":
                break
        return len(word)
            

            