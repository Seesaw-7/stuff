# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        cnt = 1
        left_node = None
        prev_left_node = None
        prev = None
        while curr:
            temp = curr.next
            if cnt == left - 1:
                prev_left_node = curr
            elif cnt == left:
                left_node = curr
                curr.next = None
            elif left < cnt < right:
                curr.next = prev
            elif cnt == right:
                curr.next = prev
                if prev_left_node:
                    prev_left_node.next = curr
                else:
                    head = curr
            elif cnt == right + 1:
                left_node.next = curr

            cnt += 1
            prev = curr
            curr = temp

        return head

    # more elegant, but I cannot code like that
    # https://leetcode.com/problems/reverse-linked-list-ii/solutions/30672/python-one-pass-iterative-solution/?envType=study-plan-v2&envId=top-interview-150
        