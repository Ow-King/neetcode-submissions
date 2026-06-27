class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = defaultdict(int)
        maxLen = 0
        maxFreq = 0

        for r in range(len(s)):
            count[s[r]] += 1 # Increment the count of the number of this letter in the frame by 1
            maxFreq = max(maxFreq, count[s[r]]) # See if this new value makes it the new top dog

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, (r - l + 1))

        return maxLen
        