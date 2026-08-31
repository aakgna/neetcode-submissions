"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head == None:
            return None
        track = dict()
        curr = head
        while curr != None:
            track[id(curr)] = Node(curr.val, None, None)
            curr = curr.next
        assign = head
        while assign != None:
            nod = track[id(assign)]
            nex = None
            if assign.next != None:
                nex = id(assign.next)
                nod.next = track[nex]
            ran = None
            if assign.random != None:
                ran = id(assign.random)
                nod.random = track[ran]
            
            assign = assign.next
        return track[id(head)]
