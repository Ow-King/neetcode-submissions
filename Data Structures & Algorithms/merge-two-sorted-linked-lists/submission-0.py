# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        onePtr = list1
        twoPtr = list2

        if (list1 is None):
            return list2
        if (list2 is None):
            return list1

        if (list1.val < list2.val):
            cur = onePtr
            output = cur
            onePtr = onePtr.next
        else:
            cur = twoPtr
            output = cur
            twoPtr = twoPtr.next

        while onePtr != None or twoPtr != None:
            if onePtr is None:
                cur.next = twoPtr
                cur = twoPtr
                twoPtr = twoPtr.next
            elif twoPtr is None:
                cur.next = onePtr
                cur = onePtr
                onePtr = onePtr.next
            else:
                if (onePtr.val < twoPtr.val):
                    cur.next = onePtr
                    cur = onePtr
                    onePtr = onePtr.next
                else:
                    cur.next = twoPtr
                    cur = twoPtr
                    twoPtr = twoPtr.next


        return output