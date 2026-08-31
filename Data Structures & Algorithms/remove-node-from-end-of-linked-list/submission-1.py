# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        total = 0
        while curr != None:
            curr = curr.next
            total += 1
        idx = total - n
        if idx == 0:
            prev = head
            curr = prev.next
            prev.next = None
            return curr
        elif n == 1:
            curr = head
            while idx != 1:
                curr = curr.next
                idx -= 1
            curr.next = None
            return head
        curr = head
        while idx != 1:
            curr = curr.next
            idx -= 1
        delete = curr.next
        after = delete.next
        del delete
        curr.next = after
        return head