# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid
        slow = head
        fast = head.next
        while fast:
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
        
        # reverse second half
        prev = None
        curr = slow
        temp = slow.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev
        # weave lls together
        while head2:
            temp = head.next
            temp2 = head2.next
            head.next = head2
            head2.next = temp
            head = temp
            head2 = temp2
        if head:
            head.next = None        
