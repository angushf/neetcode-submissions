# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # use slow and fast pointer to find middle of the list
        # reverse the list between middle -> end
        # merge the first half of the list with the reversed second list
        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        

        prev = None
        curr = slow.next
        slow.next = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        firstList = head
        secondList = prev


        while firstList and secondList:
            nxt = firstList.next
            firstList.next = secondList
            nxt2 = secondList.next
            secondList.next = nxt
            secondList = nxt2
            firstList = nxt


        
