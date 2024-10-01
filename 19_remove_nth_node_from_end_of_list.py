# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        temp = dummy

        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next

        temp = dummy
        for _ in range(cnt-n-1):
            temp = temp.next
        if temp.next:
            temp.next = temp.next.next
            
        return dummy.next
    