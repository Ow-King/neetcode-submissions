class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastIndex = {}
        start = 0
        maxLen = 0

        for i, c in enumerate(s):
            if c in lastIndex and lastIndex[c] >= start:
                start = lastIndex[c] + 1

            lastIndex[c] = i
            maxLen = max(maxLen, i - start + 1)

        return maxLen
