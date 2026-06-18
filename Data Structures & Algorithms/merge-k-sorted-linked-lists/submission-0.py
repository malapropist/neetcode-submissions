# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(1001, None)
        tail = head
        cache = [1001,-1]
        while tail:
            for index, ll in enumerate(lists):
                if ll and ll.val<cache[0]:
                    cache = [ll.val, index]

            if cache[0]==1001:
                cache=[None,0]
            print(cache)
                
            if lists and lists[cache[1]]:
                tail.next = lists[cache[1]]
                lists[cache[1]] = lists[cache[1]].next
            tail = tail.next
            cache = [1001,-1]
        tail = head.next
        while tail:
            print(tail, tail.val)
            tail = tail.next
        return head.next
                