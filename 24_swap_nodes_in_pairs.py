# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        prev = None
        while temp and temp.next:
            next_temp = temp.next.next
            if prev:
                prev.next = temp.next
            else:
                head = temp.next

            prev = temp
            temp.next.next = temp
            temp.next = next_temp
            temp = next_temp

        return head

