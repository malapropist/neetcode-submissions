# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return not subRoot
        stack = [root]
        stack2 = [subRoot]
        while stack and stack2:
            node = stack.pop()
            node2 = stack2[-1]
            if node.val == node2.val:
                node2 = stack2.pop()
                if self.sameTree(node, node2):
                    return True
                else:
                    stack2 = [subRoot]
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        stack1 = [p]
        stack2 = [q]
        while stack1 or stack2:
            node = stack1.pop()
            node2 = stack2.pop()
            if not node and not node2:
                continue
            elif not (node and node2) or (node.val != node2.val):
                return False
            if node.left or node2.left:
                stack1.append(node.left)
                stack2.append(node2.left)
            if node.right or node2.right:
                stack1.append(node.right)
                stack2.append(node2.right)
        return True