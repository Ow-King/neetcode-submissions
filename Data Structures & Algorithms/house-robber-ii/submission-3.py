class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            
        optFirst = [0] * (len(nums) - 1)
        optFirst[0] = nums[0]
        optFirst[1] = max(nums[0], nums[1])

        optLast = [0] * (len(nums) - 1)
        optLast[0] = nums[1]
        optLast[1] = max(nums[1], nums[2])        

        for i in range(2, len(nums) - 1):
            optFirst[i] = max(optFirst[i-1], (optFirst[i-2] + nums[i]))
            optLast[i] = max(optLast[i-1], (optLast[i-2] + nums[i+1]))

        return max(optFirst[len(nums) - 2], optLast[len(nums) - 2])