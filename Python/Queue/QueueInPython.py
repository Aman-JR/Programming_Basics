
#! Queue in python
# Queue is the data structure which is used in the python for the data structure and used as in the form of FIFO(First in first out)


class queue:
    def __init__(self):
        self.__data = []
        self.__count = 0
        self.__front = 0

    def enqueue(self,ele):
        self.__data.append(ele)
        self.__count += 1

    def dequeue(self):
        if self.__count == 0:
            return -1
        element = self.__data[self.__front]
        self.__front += 1
        self.__count -= 1
        return element

    def size(self):
        if self.__count == 0:
            print("Queue is empty")
            return -1
        return self.__count

    def front(self):
        if self.__count == 0:
            return -1
        return self.__data[self.__front]

    def isEmpty(self):
        return self.__count == 0


Q = queue()
Q.enqueue(1)
Q.enqueue(2)
Q.enqueue(3)

while Q.isEmpty() is False:
    print(Q.front(),end = " ")
    Q.dequeue()
print(Q.dequeue())