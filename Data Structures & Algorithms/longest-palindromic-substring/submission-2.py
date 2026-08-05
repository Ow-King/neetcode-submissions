class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = 1
        palStart = 0

        if len(s) == 1:
            return s

        for i in range(len(s)):
            tempLen = 1
            # Check for an odd length palendrome
            l = i - 1
            r = i + 1
            while l > -1 and r < len(s):
                if s[l] == s[r]:
                    tempLen += 2
                    if tempLen > output:
                        output = tempLen
                        palStart = l
                else:
                    break
                l -= 1
                r += 1

            # Check for an even length palendrome
            tempLen = 1
            l = i
            r = i + 1
            while l > -1 and r < len(s):
                if tempLen == 1:
                    if s[l] == s[r]:
                        tempLen += 1
                        if tempLen > output:
                            output = tempLen
                            palStart = l
                    else:
                        break
                    l -= 1
                    r += 1
                else:
                    if s[l] == s[r]:
                        tempLen += 2
                        if tempLen > output:
                            output = tempLen
                            palStart = l
                    else:
                        break
                    l -= 1
                    r += 1
        
        return s[palStart: palStart + output]


        