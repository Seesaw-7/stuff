# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        summ = l1.val + l2.val
        carry = summ // 10
        l1.val = summ % 10
        head = l1

        while l1.next or l2.next or carry:
            if l1.next and l2.next:
                l1 = l1.next
                l2 = l2.next
                summ = l1.val + l2.val + carry
                l1.val = summ % 10
                carry = summ // 10
            elif l1.next and not l2.next:
                l1 = l1.next
                if carry:
                    summ = l1.val + 1
                    l1.val = summ % 10
                    carry = summ // 10
            elif l2.next and not l1.next:
                l2 = l2.next
                if carry:
                    summ = l2.val + carry
                    val = summ % 10
                    carry = summ // 10
                    l1.next = ListNode(val)
                    l1 = l1.next
                else:
                    l1.next = ListNode(l2.val)
                    l1 = l1.next
            else:
                carry = 0
                new_node = ListNode(val=1)
                l1.next = new_node

        return head
