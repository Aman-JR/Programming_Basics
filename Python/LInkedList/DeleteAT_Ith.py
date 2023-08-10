class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def takeInput():
    dataList = [int(x) for x in input().split()]
    head = None
    tail = None

    for i in dataList:
        if i == -1:
            break
        newNode = Node(i)
        if head == None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode
    return head

def DeleteAt(head,i):
    if i == 0:
        head = head.next
        return head
    count = 0
    temp = head
    prev = None
    while count < i:
        prev = temp
        temp = temp.next
        count += 1

    prev.next = temp.next
    return head

def PrintLl(head):
    while head is not None:
        print(head.data, end = " ")
        head = head.next
    print("None")


head = takeInput()
print("Linked List : ",end = " ")
PrintLl(head)

p = int(input("Enter the position you want to delete form the linked list : "))
head = DeleteAt(head,p)
print("After deleting the element from the linked list : ")
PrintLl(head)