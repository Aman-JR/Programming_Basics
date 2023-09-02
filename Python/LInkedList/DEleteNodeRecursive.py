# Delete the node of teh linked list in the python

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def takeInput():
    inputList = [int(x) for x in input().split()]

    head = None
    tail = None
    for i in inputList:
        if i == -1:
            break
        newNode = Node(i)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def printLL(head):
    while head is not None:
        print((head.data), end = " ")
        head = head.next
    print('None')

def DeleteNode(head,i):
    if head is None:
        return

    if i == 0:
        tail = head.next
        return tail
    head.next = DeleteNode(head.next,i-1)
    return head

head = takeInput()
print("Linked List before the deletion of the node : ")
printLL(head)
i = int(input("ENter the position you want to delete in the Linked List : "))
print("Linked list after the deletion of the node : ")
head = DeleteNode(head,i)
printLL(head)

