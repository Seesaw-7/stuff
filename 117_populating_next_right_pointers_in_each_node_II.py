"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    # BFS 11mins
    def connect1(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = deque([(root, 0)])

        while queue:
            curr = queue.popleft()
            if not queue or queue[0][1] != curr[1]:
                curr[0].next = None
            else: 
                curr[0].next = queue[0][0]
            if curr[0].left:
                queue.append((curr[0].left, curr[1]+1))
            if curr[0].right:
                queue.append((curr[0].right, curr[1]+1))
        
        return root

    # O(N) time O(1) space
    def connect(self, root: 'Node') -> 'Node':
        head = None # left most node of the next level
        curr = root
        prev = None # previous node of the next level
        flag = 0 # end

        while curr:
            if curr.left:
                if prev == None:
                    head = curr.left
                    prev = curr.left
                else:
                    prev.next = curr.left
                    prev = curr.left
            if curr.right:
                if prev == None:
                    head = curr.right
                    prev = curr.right
                else:
                    prev.next = curr.right
                    prev = curr.right
            if curr.next:
                curr = curr.next
            else:
                curr = head
                prev = None
                head = None

        return root