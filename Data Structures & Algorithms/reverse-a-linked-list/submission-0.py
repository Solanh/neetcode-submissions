# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = head

        if not head:
            return head

        prev = None
        while s.next:
            temp = s.next
            s.next = prev

            prev = s
            s = temp

        s.next = prev
        return s

        