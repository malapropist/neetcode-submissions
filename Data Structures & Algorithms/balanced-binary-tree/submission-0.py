# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        bank = {None:(0,0)}
        stack = [root]
        while stack:
            node = stack[-1]
            if node.left and node.left not in bank:
                stack.append(node.left)
            elif node.right and node.right not in bank:
                stack.append(node.right)
            else:
                node = stack.pop()
                LH = max(bank[node.left])+1
                RH = max(bank[node.right])+1
                bank[node] = (LH,RH)
            if node in bank:
                # print(node, node in bank)
                if abs(bank[node][0]-bank[node][1])>1:
                    return False
        print(bank)
        return True