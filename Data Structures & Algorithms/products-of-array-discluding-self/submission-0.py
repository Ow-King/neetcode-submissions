class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prefix = 1
        total_suffix = 1
        prefix = []
        suffix = []
        output = []
        for i in range(0,len(nums)):
            prefix.append(total_prefix)
            suffix.append(total_suffix)
            total_prefix *= nums[i]
            total_suffix *= nums[len(nums) - i - 1]
        for i in range(0,len(nums)):
            output.append(prefix[i] * suffix[len(nums) - i - 1])
        return output