# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        
        def maxHeight(root):
            if not root:
                return 0
            
            l = maxHeight(root.left)
            r = maxHeight(root.right)

            self.diam = max(self.diam, l+r)
            return 1 + max(l, r)
        maxHeight(root)
        return self.diam