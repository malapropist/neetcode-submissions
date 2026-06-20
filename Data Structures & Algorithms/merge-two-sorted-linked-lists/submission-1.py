# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        start=dummy
        s1=list1
        s2=list2
        while s1 and s2:
            if s1.val<=s2.val:
                dummy.next=s1
                s1=s1.next
            elif s1.val>s2.val:
                dummy.next=s2
                s2=s2.next
            dummy=dummy.next
        dummy.next=max(s1,s2,key=lambda x:x is not None)
        
        return start.next
            