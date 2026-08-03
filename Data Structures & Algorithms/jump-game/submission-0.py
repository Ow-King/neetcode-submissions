class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums) - 1

        for num in range(len(nums) - 2, -1, -1):
            if num + nums[num] >= end:
                end = num

        return end == 0



        