class Solution:
    def rob(self, nums: List[int]) -> int:
        opt = [nums[0]] * len(nums)

        if len(nums) > 1:
            opt[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            opt[i] = max(opt[i-1], (opt[i-2] + nums[i]))

        return opt[len(nums) - 1]

        