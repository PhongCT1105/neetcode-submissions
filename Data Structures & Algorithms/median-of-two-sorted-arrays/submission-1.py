class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        l, r = 0, 0
        nums = []
        while l < len(nums1) and r < len(nums2):
            if nums1[l] <= nums2[r]:
                nums.append(nums1[l])
                l += 1
            else:
                nums.append(nums2[r])
                r += 1

        while l < len(nums1):
            nums.append(nums1[l])
            l += 1
        while r < len(nums2):
            nums.append(nums2[r])
            r += 1
        
        n = len(nums)
        # If even: median = avg of two middle
        if n % 2 == 0:
            return (nums[n//2-1] + nums[n//2]) / 2

        # If odd: median = middle
        if n % 2 == 1:
            return nums[n//2]