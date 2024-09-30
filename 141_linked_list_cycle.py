# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # fast and slow pointers
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast = head
        slow = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    # set
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set([head])

        while head and head.next:
            head = head.next
            if head in visited:
                return True
            visited.add(head)

        return False
