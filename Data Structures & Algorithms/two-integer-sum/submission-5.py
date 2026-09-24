class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        nums_map = {}
        for index, num in enumerate(nums):
            missing = target - num
            if missing in nums_map:
                return [nums_map[missing], index]
            else:
                nums_map[num] = index

        return [-1,-1]