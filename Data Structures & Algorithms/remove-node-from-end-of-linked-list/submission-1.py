# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # reverse LL
        # traverse from beginning and remove node
        # reverse LL again and return head

        def reverseList(head):
            if head == None or head.next == None:
                return head

            newReversedListHead = reverseList(head.next)
            head.next.next = head
            head.next = None
            return newReversedListHead

        reversedList = reverseList(head)

        currNode = reversedList
        count = 1
        while currNode != None:
            if n - 1 == 0:
                # delete head not logic
                reversedList = reversedList.next
                break

            if count == n - 1:
                # delete logic for non-head nodes
                next = currNode.next.next
                currNode.next = next
            
            currNode = currNode.next
            count += 1

        reversedList = reverseList(reversedList)
        return reversedList
