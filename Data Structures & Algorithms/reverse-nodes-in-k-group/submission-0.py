# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_k_n(self, curr, k):
        for i in range(k):
            if not curr:
                return None
            curr = curr.next
        return curr

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy
        

        while True:
            # find the initial tail of the grouping as a distance from the GPrev
            kth = self.get_k_n(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # initialize the vars for reversal section
            prev = groupNext
            curr = groupPrev.next

            # reverse the group
            for i in range(k):
                # cache state and reverse node
                temp = curr.next
                curr.next = prev
                # advance nodes
                prev = curr
                curr = temp

            # re-reverse the head node to point to the next group head
            groupTemp = groupPrev.next
            groupPrev.next = kth
            groupPrev = groupTemp
        return dummy.next