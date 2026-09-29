class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = 0
        # Convert array into set
        nums_set = set()
        for num in nums:
            if num not in nums_set:
                nums_set.add(num)

        # Loop to find the start and update res
        for num in nums:
            cnt = 1
            if num-1 in nums_set:
                continue
            while num+1 in nums_set:
                cnt += 1
                num += 1
            res = max(res, cnt)

        return res