# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        

        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        rev = slow.next
        slow.next = None
        if head.next:
            temp = rev.next
            rev.next = None
            prev = rev
            rev = temp

            while rev:
                temp = rev.next
                rev.next = prev
                prev = rev
                rev = temp

            rev = prev
            s1 = head

            while s1 and rev:
                
                n_s1 = s1.next
                n_rev = rev.next
                s1.next = rev
                rev.next = n_s1
                s1 = n_s1
                rev = n_rev

        
        