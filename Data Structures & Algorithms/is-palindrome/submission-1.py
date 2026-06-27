class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            while not s[start].isalnum() and start < end:
                start = start + 1
            while not s[end].isalnum() and start < end:
                end = end - 1

            if (s[start].lower() != s[end].lower()):
                return False
            start = start + 1
            end = end - 1 
        
        return True
    