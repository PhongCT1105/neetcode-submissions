class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        nums.sort()

        def dfs(subset, i):

            if i == len(nums):
                res.add(tuple(subset))
                return 

            subset.append(nums[i])
            i += 1
            dfs(subset, i)

            subset.pop(-1)
            dfs(subset, i)

        dfs([], 0)        
        return list(res)