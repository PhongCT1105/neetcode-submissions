class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        prev1, prev2 = 0, cost[0]

        for i in range(1, len(cost)):
            cost_at_i = min(cost[i]+prev1, cost[i]+prev2)
            prev1 = prev2
            prev2 = cost_at_i
        
        return min(prev1,prev2)