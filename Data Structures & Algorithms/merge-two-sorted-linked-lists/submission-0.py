# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        mergedListHead = ListNode(0)
        mergedCurrPtr = mergedListHead

        while head1 != None and head2 != None:
            nextFrom1 = head1.val
            nextFrom2 = head2.val

            if nextFrom1 <= nextFrom2:
                mergedCurrPtr.next = head1
                head1 = head1.next
                mergedCurrPtr = mergedCurrPtr.next
            else:
                mergedCurrPtr.next = head2
                head2 = head2.next
                mergedCurrPtr = mergedCurrPtr.next

        if head1 == None:
            mergedCurrPtr.next = head2
        
        if head2 == None:
            mergedCurrPtr.next = head1

        return mergedListHead.next

            

            