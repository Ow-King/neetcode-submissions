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
            if (slow is None):
                return False
            if (fast is None):
                return False  
            
            slow = slow.next  
            fast = fast.next

            if (fast is None):
                return False

            fast = fast.next
        
        return True
        