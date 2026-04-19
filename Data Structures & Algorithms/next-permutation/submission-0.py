class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l, r = n-1, n-2

        while r >= 0:
            if nums[r] < nums[l]:
                break
            r -= 1
            l -= 1

        if r >= 0:
            pivot = r
            index_swap = l
            for i in range(l, n):
                if nums[i] > nums[pivot] and nums[i] <= nums[index_swap]:
                    index_swap = i
            nums[pivot], nums[index_swap] = nums[index_swap], nums[pivot]
            nums[pivot+1:] = sorted(nums[pivot+1:])
        else:
            nums.sort()