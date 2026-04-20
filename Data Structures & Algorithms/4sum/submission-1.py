class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                l, r = j, len(nums)-1
                total = nums[i] + nums[j]
                left_over = target - total
                while l < r:
                    if nums[l] + nums[r] == left_over:
                        res.add(tuple([nums[i], nums[j], nums[l], nums[r]]))
                        break
                    elif nums[l] + nums[r] < left_over:
                        l += 1
                    else:
                        r -= 1
        return list(res)