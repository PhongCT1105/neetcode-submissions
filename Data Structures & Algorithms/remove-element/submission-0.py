class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l, r = 0,0

        while r < len(nums):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
            r += 1
        
        while len(nums) > l:
            nums.pop(-1)
        
        return len(nums)