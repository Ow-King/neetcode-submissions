# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True
        return False
        
    def sameTree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if root == None and subroot == None:
            return True
        if root == None or subroot == None:
            return False
        if root.val == subroot.val:
            if self.sameTree(root.left, subroot.left):
                return self.sameTree(root.right, subroot.right)
        return False