class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(index, vals, total):
            if (total == target): # append the value and return if complete
                output.append(vals.copy())
                return
            if index >= len(nums) or target < total:
                return
            
            vals.append(nums[index])
            dfs(index, vals, total + nums[index])
            vals.pop()
            dfs(index + 1, vals, total) # Skip the value and go next

        dfs(0, [], 0)
        return output
        

