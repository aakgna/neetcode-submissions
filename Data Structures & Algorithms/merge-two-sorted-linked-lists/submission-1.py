# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        elif list2 == None:
            return list1
        ans = ListNode(0)
        list3 = ans
        curr1 = list1
        curr2 = list2
        cnt = 0
        while curr1 != None and curr2 != None:
            print(curr1.val, curr2.val)
            if curr1.val < curr2.val:
                if cnt == 0:
                    list3.val = curr1.val
                else:
                    list3.next = curr1
                curr1 = curr1.next
            else:
                if cnt == 0:
                    list3.val = curr2.val
                else:
                    list3.next = curr2
                curr2 = curr2.next
            if cnt != 0:
                list3 = list3.next
            cnt += 1
        if curr1 == None:
            list3.next = curr2
        else:
            list3.next = curr1
        return ans