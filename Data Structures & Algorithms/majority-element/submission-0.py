class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        hash_map = {}
        pairs = (0, 0)

        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

            if hash_map[num] > pairs[1]:
                pairs = (num, hash_map[num])

        return pairs[0]