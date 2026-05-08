# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l, r = 0, 0
        length = 0
        currNode = head

        while currNode != None:
            length += 1
            currNode = currNode.next

        r = math.ceil(length / 2)

        currNode = head
        position = 0
        while position < r:
            currNode = currNode.next
            position += 1

        def reverseList(head):
            if head == None or head.next == None:
                return head

            reversedHeadList = reverseList(head.next)
            head.next.next = head
            head.next = None
            return reversedHeadList

        reversedList = reverseList(currNode)
        
        list1 = head
        list2 = reversedList
        ptr = list1

        while list2 != None:
            next = list2.next
            list2.next = ptr.next
            ptr.next = list2
            ptr = ptr.next.next
            list2 = next

        ptr.next = None

        print(list1.val)



