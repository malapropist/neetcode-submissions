# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]
        print(root)
        while stack:
            node = stack.pop()
            if not node:
                continue
            store = None
            if node.left:
                store = node.left
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            node.left = node.right
            node.right = store
        return root
    