# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return root

        stac = [root]
        while stac:
            print(stac)
            node = stac.pop()
            l = node.left
            r = node.right
            node.left, node.right = r, l
            if l:
                stac.append(l)
            if r:
                stac.append(r)
        return root