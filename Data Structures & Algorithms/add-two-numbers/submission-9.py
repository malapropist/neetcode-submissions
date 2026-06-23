# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
   def addTwoNumbers(self, l1, l2):
    curr = l1
    curr2 = l2
    carry = 0
    prev = None

    while curr or curr2:
        a = curr.val if curr else 0
        b = curr2.val if curr2 else 0

        total = a + b + carry
        digit = total % 10
        carry = total // 10

        if curr:
            curr.val = digit
        else:
            curr = ListNode(digit)
            prev.next = curr

        prev = curr
        curr = curr.next
        curr2 = curr2.next if curr2 else None

    if carry:
        prev.next = ListNode(carry)

    return l1