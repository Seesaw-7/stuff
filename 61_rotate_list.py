# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        num = 0
        temp = head
        if not temp:
            return None

        while temp:
            if temp.next:
                temp = temp.next
            else:
                num += 1
                break
            num += 1

        temp.next = head
        k = k % num
        temp = head
        for _ in range(num-k-1):
            temp = temp.next

        new_head = temp.next
        temp.next = None

        return new_head
    