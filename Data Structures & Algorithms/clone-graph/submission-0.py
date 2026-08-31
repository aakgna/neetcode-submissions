"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        elif len(node.neighbors) == 0:
            return Node(node.val, None)
        hist = dict()
        vis = set()
        stack = [node]

        while len(stack) > 0:
            curr = stack.pop()
            if id(curr) in vis:
                continue
            vis.add(id(curr))
            new_node = Node(curr.val)
            hist[id(curr)] = new_node
            stack.extend(curr.neighbors)

        vis = set()
        stack = [node]

        while len(stack) > 0:
            curr = stack.pop()
            loc = id(curr)
            if loc in vis:
                continue
            vis.add(loc)
            for n in curr.neighbors:
                hist[loc].neighbors.append(hist[id(n)])
            stack.extend(curr.neighbors)
        return hist[id(node)]