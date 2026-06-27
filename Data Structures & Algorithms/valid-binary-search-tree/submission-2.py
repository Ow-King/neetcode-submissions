# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        interval = [-1001, 1001]

        return self.dfs(root, interval)



    def dfs(self, root: Optional[TreeNode], interval) -> bool:
        if root == None:
            return True
        
        if not (interval[0] < root.val < interval[1]):
            return False

        leftInterval = [interval[0], min(root.val, interval[1])]
        rightInterval = [max(root.val, interval[0]), interval[1]]

        return (self.dfs(root.left, leftInterval) and self.dfs(root.right, rightInterval))
