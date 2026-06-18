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
        track = {}
        start = head

        while head:
            track[head] = Node(head.val)
            head = head.next
        head = start
        new_head = track[head] if head else None
        while head:
            track[head].next = track[head.next] if head.next else None
            track[head].random = track[head.random] if head.random else None
            head = head.next

        return new_head