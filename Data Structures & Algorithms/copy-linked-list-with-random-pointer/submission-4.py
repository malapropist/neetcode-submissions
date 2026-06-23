"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        lis = {}
        curr = head
        c_curr = curr
        while curr:
            if curr:
                copy = Node(curr.val)
                lis[curr]=copy
                curr = curr.next
            else:
                break
        curr = head
        for i in lis:
            curr = i
            if curr.random:
                lis[i].random = lis[curr.random]
            if curr.next:
                lis[i].next = lis[curr.next]
        ans = lis[c_curr] if c_curr else None
        return ans


