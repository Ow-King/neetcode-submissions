class Solution:
    def numDecodings(self, s: str) -> int:
        
        # ones digit < 10 - 1-9 

        # Tens digit - 1 or 2
            # ones digit - 10 - 0-9

            # ones digit - 10 - 0-6


        # 1-9, after a 1 add 2 options - unless previous value has a score > 2, in 
        # 1-6, after a 2 adds 2 options

        # 0 after anything but a 1 or a 2 makes it invalid, after a 1 or a 2 it adds no additional options

        dp = { len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i + 1)
            if (i + 1 < len(s)) and ((s[i] == "1") or (s[i] == "2" and s[i+1] in "0123456")):
                res += dfs(i+2)
            
            dp[i] = res

            return res

        return dfs(0)

        
