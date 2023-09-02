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

def InsertAt(head,k,num):
    count = 0
    temp = head
    prev = None
    while count < k:
        prev = temp
        temp = temp.next
        count = count+1
    newNode = Node(num)
    if prev is not None:
        prev.next = newNode 
    else:
        head = newNode
    newNode.next = temp
    return head

def PrintLL(head):
    while head is not None:
        print((head.data),end=" ")
        head = head.next
    print("None")


head = takeInput()
print("Linked List : ",end = " ")
PrintLL(head)

k = int(input("Enter the position where you want to insert the data in the linked list : "))
num = int(input("Enter the data you want to enter in the linked list : "))
head = InsertAt(head,k,num)
PrintLL(head)
