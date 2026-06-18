# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, -101)]
        ans = 0
        while stack:
            node, maxval = stack.pop()
            if node.val >= maxval:
                ans+=1
                maxval = node.val
            if node.left:
                stack.append((node.left,maxval))
            if node.right:
                stack.append((node.right,maxval))
        return ans