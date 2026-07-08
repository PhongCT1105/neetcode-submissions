class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        n = len(nums)
        for i in range(n):
            if target-nums[i] in hash_map: # Match
                return [hash_map[target-nums[i]],i]
            else:
                hash_map[nums[i]] = i
        