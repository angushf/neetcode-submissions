"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Init dictionary to store old nodes as keys and new nodes as values
        myDict = {}
        # Init currPtr 
        currPtr = head
        newHead = None
        newHeadPtr = newHead
        # currPtr traverses the LL and creates new nodes that don't exist
        # in dict and uses values for keys that exist in dict
        while currPtr != None:
            if currPtr not in myDict:
                newNode = Node(currPtr.val)
                myDict[currPtr] = newNode
                if newHead is None:
                    newHead = newNode
            
            newHeadPtr = myDict[currPtr]

            if currPtr.random not in myDict:
                newRandomNode = None
                if currPtr.random == None:
                    newRandomNode = None
                else:
                    newRandomNode = Node(currPtr.random.val)

                newHeadPtr.random = newRandomNode
                myDict[currPtr.random] = newRandomNode
            else:
                newRandomNode = myDict[currPtr.random]
                newHeadPtr.random = newRandomNode

            if currPtr.next not in myDict:
                newNextNode = None
                if currPtr.next == None:
                    newNextNode = None
                else:
                    newNextNode = Node(currPtr.next.val)
                    myDict[currPtr.next] = newNextNode

                newHeadPtr.next = newNextNode
            else:
                newNextNode = myDict[currPtr.next]
                newHeadPtr.next = newNextNode

            newHeadPtr = newHeadPtr.next
            currPtr = currPtr.next

        return newHead

            