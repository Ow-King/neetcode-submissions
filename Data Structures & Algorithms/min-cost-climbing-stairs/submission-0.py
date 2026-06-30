class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        optCost = [None] * (len(cost) + 1)

        def dp(i):
            if i <= 1:
                optCost[i] = 0
            else:
                optCost[i] = min(optCost[i-1] + cost[i-1], optCost[i-2] + cost[i-2])
        
        for i in range(len(optCost)):
            dp(i)

        return optCost[len(optCost) - 1]