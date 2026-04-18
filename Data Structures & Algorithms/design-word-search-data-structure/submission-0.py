class WordDictionary:

    def __init__(self):
        self.array = []

    def addWord(self, word: str) -> None:
        self.array.append(word)

    def search(self, word: str) -> bool:
        for element in self.array:
            if len(element) != len(word):
                continue
            cnt = 0
            for c in element:
                if word[cnt] == c or word[cnt] == ".":
                    cnt += 1
                else:
                    break
            if cnt == len(word):
                return True

        return False