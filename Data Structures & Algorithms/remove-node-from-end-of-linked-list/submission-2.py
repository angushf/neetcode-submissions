# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Find length of LL
        listLength = 0
        currNode = head

        while currNode != None:
            listLength += 1
            currNode = currNode.next

        # Calculate offset from beginning of list 
        # e.g., if length is 10 and we want to delete 2nd from end, 
        # that is 10-2=8 from beginning of list.
        offset = listLength - n

        # Iterate through LL to delete 8th node
        currNode = head
        index = 1

        while index < offset:
            currNode = currNode.next
            index += 1

        if offset == 0:
            head = head.next
        else:
            next = currNode.next.next
            currNode.next = next

        return head
        
