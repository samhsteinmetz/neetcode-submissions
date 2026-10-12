# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Consider building a new sorted list (or maintaining a sorted portion)     node by node. Using a **dummy node** at the front of the sorted       list can simplify edge cases when inserting a node at the very beginning.
        dummy = ListNode(0)
        

        while head:
            lVal = head.val
            curr = dummy
            while curr.next and lVal > curr.next.val:
                curr = curr.next
            curr.next = ListNode(lVal, curr.next)
            head = head.next
        return dummy.next



        