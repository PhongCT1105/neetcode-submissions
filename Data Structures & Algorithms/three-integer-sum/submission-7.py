class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(0, n-2):
            hash_map = set()
            target = -nums[i]
            for j in range(i+1, n):
                needed = target - nums[j]
                if needed in hash_map:
                    res.add((nums[i],needed,nums[j]))
                else:
                    hash_map.add(nums[j])
        return list(res)