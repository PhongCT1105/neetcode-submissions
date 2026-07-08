class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = set()
        for num in nums:
            hash_map.add(num)
        res = 0
        for num in nums:
            if num-1 in hash_map:
                continue
            cnt = 1
            while num+1 in hash_map:
                cnt += 1
                num += 1
            res = max(res, cnt)
        return res