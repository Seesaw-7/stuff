# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyhead = ListNode()
        dummyhead.next = head

        prev, curr = dummyhead, head
        while True:
            cnt = 1
            left_reserved = curr

            while curr and cnt < k:
                curr = curr.next
                cnt += 1
                if not curr:
                    return dummyhead.next

            prev.next, curr = curr, prev.next
            if not curr:
                return dummyhead.next
            prev, curr = curr, curr.next

            for _ in range(k-1):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            prev = left_reserved
            prev.next = curr

        return dummyhead.next
