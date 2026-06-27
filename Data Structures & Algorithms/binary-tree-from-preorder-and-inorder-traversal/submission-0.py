# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        indices = {val: idx for idx, val in enumerate(inorder)} # Make a hash map to make sure that it is not N^2

        self.pre_idx = 0 # Identify that the first node in the pre index is the head

        def dfs(l, r):
            if l > r: # Check to see if you have gone too far
                return None
            
            root_val = preorder[self.pre_idx] # preorder is always going to be the next node to add
            self.pre_idx += 1
            root = TreeNode(root_val) # set the root of the next part you constuct to that pre val

            mid = indices[root_val] # find midpoint in the indecies to know what other nodes are on the side of the tree
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(preorder) - 1)