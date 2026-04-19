class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                for k in range(j+1, len(nums)-1):
                    for l in range(k+1, len(nums)):
                        total = nums[i] + nums[j] + nums[k] + nums[l]
                        if total == target:
                            total = tuple(sorted([nums[i], nums[j], nums[k], nums[l]]))
                            if total not in res:
                                res.add(total)
        return list(res)