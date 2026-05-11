# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def extractNumber(head):
            currNode = head
            number = []

            while currNode != None:
                number.append(currNode.val)
                currNode = currNode.next

            return number

        def reverseList(head):
            if head == None or head.next == None:
                return head

            newListHead = reverseList(head.next)
            head.next.next = head
            head.next = None
            return newListHead

        # Reverse both LL's
        reversed_l1 = reverseList(l1)
        reversed_l2 = reverseList(l2)

        # Iterate both LL's and at each node, add val to its own global array
        number_l1 = extractNumber(reversed_l1)
        number_l2 = extractNumber(reversed_l2)

        # Convert both arrays into numbers
        clean_number_l1 = int("".join(str(x) for x in number_l1))
        clean_number_l2 = int("".join(str(x) for x in number_l2))

        # Add said numbers together
        result = clean_number_l1 + clean_number_l2

        # Convert final result from number -> string
        str_result = str(result)
        print(str_result)

        # Create new LL using final result
        newList = None
        ptr = newList
        str_result_length = len(str_result)
        index = 0

        while index < str_result_length:
            if index == 0:
                newList = ListNode(int(str_result[index]))
                ptr = newList
            else:
                ptr.next = ListNode(int(str_result[index]))
                ptr = ptr.next

            index += 1
        # Reverse LL using function def
        answer = reverseList(newList)
        return answer