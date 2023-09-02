
class Node:
    def __init__(self,initData):
        self.data = initData
        self.next = None


class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def push(self,element):
        newNode = Node(element)
        newNode.next = self.__head
        self.__head = newNode
        self.__count += 1

    def pop(self):
        if self.isEmpty() is True:
            print("Stack is empty")
            return
        data = self.__head.data
        self.__head = self.__head.next
        self.__count -= 1
        return data
    def top(self):
        if self.isEmpty() is True:
            print("Stack is Empty")
            return
        data = self.__head.data
        return data
    def size(self):
        return self.__count
    def isEmpty(self):
        return self.size() == 0


s = Stack()
n = int(input("Enter the size of the stack : "))
for i in range(0,n):
    a = int(input())
    s.push(a)


print("Stack : ")
while s.isEmpty() is False:
    print(s.pop(),end = " ")
print()
s.top()
