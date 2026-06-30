class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        optCost = [0] * (len(cost) + 1)

        def dp(i):
            optCost[i] = min(optCost[i-1] + cost[i-1], optCost[i-2] + cost[i-2])
        
        for i in range(2, len(optCost)):
            dp(i)

        return optCost[len(optCost) - 1]