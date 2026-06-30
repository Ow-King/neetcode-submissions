class Solution:
    def climbStairs(self, n: int) -> int:
        optHeight = [None] * n

        def dp(idx):
            if (idx == 0):
                optHeight[idx] = 1
                return 1
            if (idx == 1):
                optHeight[idx] = 2
                return 2
            steps = optHeight[idx-1] + optHeight[idx-2]
            optHeight[idx] = steps
            return steps

        for i in range(n):
            dp(i)
        
        return optHeight[n - 1]