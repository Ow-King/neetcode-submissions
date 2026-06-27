# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smallNode = min(p.val, q.val)
        bigNode = max(p.val, q.val)
        cur = root
        decendent = False

        while (not decendent):
            if (cur.val >= smallNode):
                if (cur.val <= bigNode):
                    return cur
                else:
                    cur = cur.left
            else:
                cur = cur.right

        