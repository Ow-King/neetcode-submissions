class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        count = defaultdict(int)
        minLen = float('inf') 
        out = ""

        for r in range(len(t)): # Set up how many letters we need
            count[t[r]] += 1


        for r in range(len(s)):
            if s[r] in count: # decrement how many letters needed for a desired substing
                count[s[r]] -= 1
            
            while max(count.values()) <= 0: # if all letters are missing move the left bound up until there is a 0 again
                if max(count.values()) == 0: # if all letters are satisfied check if this is the minimim window substring
                    if (r - l + 1) < minLen:
                        out = s[l:(r + 1)]
                        minLen = r - l + 1

                if s[l] in count:
                    count[s[l]] += 1
                l += 1
    
                

        return out
