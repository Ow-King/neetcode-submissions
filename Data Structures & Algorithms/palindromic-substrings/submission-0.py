class Solution:
    def countSubstrings(self, s: str) -> int:
        oddPalendromes = [1] * len(s)
        evenPalendromes = [0] * len(s)

        for i in range(len(s)):
            # Check for an odd length palendrome
            l = i - 1
            r = i + 1
            while l > -1 and r < len(s):
                if s[l] == s[r]:
                    oddPalendromes[i] += 1
                else:
                    break
                l -= 1
                r += 1

            # Check for an even length palendrome
            l = i
            r = i + 1
            while l > -1 and r < len(s):
                if s[l] == s[r]:
                    evenPalendromes[i] += 1
                else:
                    break
                l -= 1
                r += 1
        
        return sum(oddPalendromes) + sum(evenPalendromes)