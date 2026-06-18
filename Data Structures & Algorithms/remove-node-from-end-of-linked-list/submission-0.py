# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 1
        pointer = head
        while pointer:
            length += 1
            pointer = pointer.next
        target = length - n

        prev = None
        curr = head
        for i in range(target-1):
            prev = curr
            curr = curr.next
        if prev:
            prev.next = curr.next
            return head
        elif curr:
            return head.next
        else:
            return None

