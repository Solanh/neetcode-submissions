# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        check_count = head
        count = 0

        while check_count:
            check_count = check_count.next
            count += 1

        rem = count - (n-1)

        tail = head
        idx = 1
            
        if rem == idx:
            return head.next
        
        while tail:
            if idx == rem -1:
                if tail.next:
                    tail.next = tail.next.next
                
                
            
            tail = tail.next
            idx += 1

        return head
            

        