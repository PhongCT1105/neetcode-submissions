class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l < r: 
                if nums[l] + nums[r] < -nums[i]:
                    l += 1
                elif nums[l] + nums[r] > -nums[i]:
                    r -= 1
                else:
                    res.add(tuple([nums[i], nums[l], nums[r]]))
                    l += 1
                    r -= 1
              
        return list(res)