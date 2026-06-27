class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for x in range(len(nums) - 2):
            left = x
            middle = x + 1
            right = x + 2

            while left >= 0 and right < len(nums):
                value = nums[left] + nums[middle] + nums[right]
                if value == 0:
                    tup = [nums[left], nums[middle], nums[right]]
                    if tup not in output:
                        output.append([nums[left], nums[middle], nums[right]])
                    left = left - 1
                    right = right + 1
                if value > 0:
                    left = left - 1
                if value < 0:
                    right = right + 1

        return output

        