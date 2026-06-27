class Solution:
    #def maxProfit(self, prices: List[int]) -> int:
    #    l = 0
    #    r = len(prices) - 1
    #    max = prices[r] - prices[l]
#
    #    while (l != r):
    #        if ((prices[r] - prices[l+1]) >= (prices[r-1] - prices[l])):
    #            l = l + 1
    #        else:
    #            r = r - 1
#
    #        temp = (prices[r] - prices[l])
    #        if (temp > max):
    #            max = temp
    #    
    #    return max

    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max = 0

        while (r < len(prices)):
            if (prices[r] < prices[l]): # If you find a new minimum start from there in the future
                l = r
            else:
                temp = (prices[r] - prices[l])
                if (temp > max):
                    max = temp
            r = r + 1
        
        if max < 0:
            max = 0

        return max
        