class TrieNode: 
    def __init__(self):
        self.child = [None] * 26
        self.isEndofWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Build a prefix tree of words first:
        word_lib = TrieNode()
        for word in words:
            curr = word_lib
            for c in word:
                idx = ord(c) - ord('a')
                if not curr.child[idx]:
                    curr.child[idx] = TrieNode()
                curr = curr.child[idx]
            curr.isEndofWord = True

        # DFS through the board with visit
        ROWS, COLS = len(board), len(board[0])
        visited = set()
        res = set()
        for r in range(ROWS):
            for c in range(COLS):
                def dfs(r, c, word, curr):
                    # Out of range => return:
                    if not 0 <= r < ROWS or not 0 <= c < COLS:
                        return
                    # Already visited:
                    if (r,c) in visited:
                        return
                    # Get index 
                    letter = board[r][c]
                    idx = ord(letter) - ord('a')
                    # If not child in the vocab => return
                    if not curr.child[idx]:
                        return

                    visited.add((r,c))
                    word.append(board[r][c])
                    curr = curr.child[idx]
                    # Check if end of words:
                    if word and curr.isEndofWord:
                        res.add("".join(word))

                    dfs(r-1, c, word, curr)
                    dfs(r+1, c, word, curr)
                    dfs(r, c-1, word, curr)
                    dfs(r, c+1, word, curr)
                    visited.discard((r,c))
                    word.pop(-1)
                dfs(r, c, [], word_lib)
        return list(res)