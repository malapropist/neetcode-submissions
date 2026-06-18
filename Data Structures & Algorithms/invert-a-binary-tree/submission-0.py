# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def inv_node(root):
            if root:
                temp = root.left
                root.left = root.right
                root.right = temp
                if root.left:
                    inv_node(root.left)
                if root.right:
                    inv_node(root.right)
            return root
        return inv_node(root)