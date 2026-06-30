class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        opt = [nums[0]] * len(nums)
        opt[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            opt[i] = max(opt[i-1], (opt[i-2] + nums[i]))

        return opt[len(nums) - 1]

        