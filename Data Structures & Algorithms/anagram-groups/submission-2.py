class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def return_map(s):
            arr = [0] * 26
            for c in s:
                arr[ord(c)-ord('a')] += 1
            return arr
        res = {}
        for word in strs:
            word_map = tuple(return_map(word))
            if word_map in res:
                res[word_map].append(word)
            else:
                res[word_map] = [word]

        return list(res.values())