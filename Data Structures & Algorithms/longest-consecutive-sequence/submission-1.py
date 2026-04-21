class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_num = set(nums)
        res = 0

        for i in range(len(nums)):
            cnt = 1
            j = 1
            while nums[i]+j in hash_num:
                cnt += 1
                j += 1
            res = max(res, cnt)
        return res