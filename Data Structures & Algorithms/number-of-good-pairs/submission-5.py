class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        hash_map = {}

        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1
        
        res = 0
        for num in hash_map.values():
            if num > 1:
                res += num * (num-1) // 2
        return res