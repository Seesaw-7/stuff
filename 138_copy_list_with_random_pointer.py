"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    # use list
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_list = Node(0)
        dummy_new_head = new_list
        dummy_old_head = head
        new_nodes = []
        old_nodes = []

        while head:
            old_nodes.append(head)
            new_node = Node(0)
            new_list.next = new_node
            new_list.next.val = head.val
            new_nodes.append(new_node)
            new_list = new_list.next
            head = head.next

        head = dummy_old_head
        new_list = dummy_new_head.next

        while head:
            if head.random == None:
                new_list.random = None
            else:
                i = old_nodes.index(head.random)
                new_list.random = new_nodes[i]
            head = head.next
            new_list = new_list.next

        return dummy_new_head.next

    # use hashtable
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_list = Node(0)
        dummy_new_head = new_list
        dummy_old_head = head
        new_nodes = {}
        old_nodes = {}

        cnt = 0
        while head:
            old_nodes[head] = cnt
            new_node = Node(0)
            new_list.next = new_node
            new_list.next.val = head.val
            new_nodes[cnt] = new_node
            new_list = new_list.next
            head = head.next
            cnt += 1

        head = dummy_old_head
        new_list = dummy_new_head.next

        while head:
            if head.random == None:
                new_list.random = None
            else:
                i = old_nodes[head.random]
                new_list.random = new_nodes[i]
            head = head.next
            new_list = new_list.next

        return dummy_new_head.next

    # better coding with hashtable, hashing from old nodes to new nodes
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new = {}

        curr = head
        while curr:
            old2new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            old2new[curr].next = old2new[curr.next] if curr.next != None else None
            old2new[curr].random = old2new[curr.random] if curr.random != None else None
            curr = curr.next

        return old2new[head] if head else None

    # use dict.get()
    # but seems to be a bit slow
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old2new = {}

        curr = head
        while curr:
            old2new[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            old2new[curr].next = old2new.get(curr.next)
            old2new[curr].random = old2new.get(curr.random)
            curr = curr.next

        return old2new.get(head)

    # with O(1) space:
    # https://leetcode.com/problems/copy-list-with-random-pointer/solutions/43491/a-solution-with-constant-space-complexity-o-1-and-linear-time-complexity-o-n/?envType=study-plan-v2&envId=top-interview-150
