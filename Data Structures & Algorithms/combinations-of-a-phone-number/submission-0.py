class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        num_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        ptr = 0
        res = []

        def dfs(word, ptr):
            # Edge case: ptr reach end, no more digits
            if ptr == len(digits):
                res.append("".join(word[:]))
                return
            
            num = digits[ptr]
            for letter in num_map[num]:
                word.append(letter)
                dfs(word, ptr+1) 
                word.pop(-1)

        dfs([], 0)        
        return res
            

