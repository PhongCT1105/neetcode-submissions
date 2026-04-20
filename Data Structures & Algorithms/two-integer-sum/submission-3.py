class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(nums)):
            left_over = target - nums[i]
            if left_over in hash_map:
                return [hash_map[left_over], i]
            hash_map[nums[i]] = i