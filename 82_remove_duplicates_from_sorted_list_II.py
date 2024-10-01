# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        appeared = set()
        remove = set()
        
        dummy = ListNode()
        dummy.next = head

        temp = head

        while temp:
            if temp.val in appeared:
                remove.add(temp.val)
            else:
                appeared.add(temp.val)
            temp = temp.next

        prev, curr = dummy, head
        while curr:
            if curr.val in remove:
                prev.next = curr.next
                curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return dummy.next

    # since it's sorted, it can be done with one iteration