class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        
        for word in strs:
            cnt_map = [0] * 26
            for c in word:
                cnt_map[ord(c) - ord('a')] += 1
            cnt_map = tuple(cnt_map)
            if cnt_map in hash_map:
                hash_map[cnt_map].append(word)
            else:
                hash_map[cnt_map] = [word]
            
        return list(hash_map.values())