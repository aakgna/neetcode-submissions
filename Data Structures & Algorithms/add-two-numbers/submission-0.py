# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rev(self, s: str) -> str:
        return s[::-1]
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        arr1 = ""
        while curr1 != None:
            arr1 += str(curr1.val)
            curr1 = curr1.next
        curr2 = l2
        arr2 = ""
        while curr2 != None:
            arr2 += str(curr2.val)
            curr2 = curr2.next
        arr1 = self.rev(arr1)
        arr2 = self.rev(arr2)
        val = str(int(arr1) + int(arr2))
        val = self.rev(val)
        final = ListNode(int(val[0]), None)
        curr = final
        for i in range(1, len(val)):
            res = ListNode(int(val[i]), None)
            curr.next = res
            curr = curr.next
        return final