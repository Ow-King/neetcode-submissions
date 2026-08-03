class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        jumps = 0
        maxJump = []
        for i in range(len(nums) - 1):
            maxJump.append(i + nums[i])

        while r < len(nums) - 1:
            farthest = max(maxJump[l:r+1])
            l = r + 1
            r = farthest
            jumps += 1
        
        return jumps

        