# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        dq = [(root,0)]
        ans = []
        while dq:
            node_pair = dq.pop()
            node = node_pair[0]
            depth = node_pair[1]
            print((node.val if node else None, depth))

            if not node:
                continue
            if depth==len(ans):
                ans.append(node.val)
            dq.append((node.left, depth+1))
            dq.append((node.right, depth+1))

        return ans