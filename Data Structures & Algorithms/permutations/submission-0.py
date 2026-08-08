class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []

        for perm in perms:
            for i in range(len(perms) + 1):
                newPerm = perm.copy()
                newPerm.insert(i, nums[0])
                if newPerm not in res:
                    res.append(newPerm)

        return res
        