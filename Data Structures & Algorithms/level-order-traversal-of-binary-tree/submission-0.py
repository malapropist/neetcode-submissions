# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stack = [(root,0)] # (node, row)
        ans = []
        while stack:
            node = stack.pop()
            row = node[1]
            node = node[0]
            if not node:
                continue
            if len(ans)==row:
                ans.append([])
            ans[row].append(node.val)
            if node.right:
                stack.append((node.right, row+1))
            if node.left:
                stack.append((node.left, row+1))
        return ans