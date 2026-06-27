# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None): 
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        

        if slow is None:
            return False
        fast = slow.next

        while fast != slow:
            slow = slow.next

            if (slow is None):
                return False
            
            if (fast.next is None):
                return False
            
            fast = fast.next.next

            if (fast is None):
                return False
        
        return True
        