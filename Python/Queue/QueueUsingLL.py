class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
    
    def enqueue(self,data):
        if self.__head == None:
            newNode = Node(data)
            self.__head = newNode
            self.__tail = newNode
            self.__count += 1
        else:
            newNode = Node(data)
            self.__tail.next = newNode
            self.__tail = newNode
            self.__count += 1
    
    def dequeue(self):
        if self.__head is None:
            return -1
        else:
            self.__head = self.__head.next
            self.__count -= 1
    
    def front(self):
        ele = self.__head.data
        return ele
    
    def size(self):
        return self.__count
    
    def isEmpty(self):
        return self.__count == 0
    

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

while q.isEmpty() is False:
    print(q.front())
    q.dequeue()

print(q.dequeue())



