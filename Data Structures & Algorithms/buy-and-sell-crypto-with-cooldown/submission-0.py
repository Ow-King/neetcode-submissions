class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #[4] => 0 C
        #[0, 4] -> 4 B, S
        #[4, 0, 4] -> 4 C, B, S

        dp = {} # key = (i, buying) val = max profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i,buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                cooldown = dfs(i+1, buying)
                dp[(i,buying)] = max(sell, cooldown)

            return dp[(i,buying)]

        return dfs(0, True)
