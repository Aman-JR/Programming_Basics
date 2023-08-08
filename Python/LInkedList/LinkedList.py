
#! O(n2) time complexity for creating the linked list
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None

# def takeInput():
#     inputList = [int(x) for x in input().split()]
#     head = None

#     for i in inputList:
#         if  i == -1:
#             break
#         newNode = Node(i)
#         if head is None:
#             head = newNode
#         else:
#             tail = head
#             while tail.next is not None:
#                 tail = tail.next
#             tail.next = newNode
#     return head

# def PrintLL(head):
#     while head is not None:
#         print(str(head.data) + " ->", end = " ")
#         head = head.next
#     print("None")
#     return


# head = takeInput()
# PrintLL(head)


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

def PrintLL(head):
    while head is not None:
        print(str(head.data) + "->",end = "")
        head = head.next
    print("None")
    return

head = takeInput()
PrintLL(head)
