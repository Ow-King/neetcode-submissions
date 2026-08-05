class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        output = -10001
        for num in nums:
            cur += num
            if cur > output:
                output = cur
            if cur < 0:
                cur = 0
        return output

        