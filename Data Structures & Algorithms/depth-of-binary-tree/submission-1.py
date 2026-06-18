# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = 1
        stac = [(root,1)]
        while stac:
            pair = stac.pop()
            node, count = pair[0], pair[1]
            if node.left: stac.append((node.left, count+1))
            if node.right: stac.append((node.right, count+1))
            ans = max(count, ans)
        return ans