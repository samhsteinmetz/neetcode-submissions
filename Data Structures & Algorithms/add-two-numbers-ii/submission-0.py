# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def helpNumber(head, lis):
            lis.append(str(head.val))
            if head.next == None:
                ret = ''.join(lis)
                print(ret)
                return ret
            return helpNumber(head.next, lis)
        
        number1 = helpNumber(l1, [])
        number2 = helpNumber(l2, [])

        # dummy = ListNode(-)
        totalStr = str(int(number1) + int(number2))

        dummy = ListNode(0)
        curr = dummy

        print(totalStr)

        for dig in totalStr:
            curr.next = ListNode(int(dig))
            curr = curr.next


        


        return dummy.next


        