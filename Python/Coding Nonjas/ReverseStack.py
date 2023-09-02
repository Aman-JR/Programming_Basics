
class Stack:
    def __init__(self):
        self.__data = []

    def push(self,ele):
        self.__data.append(ele)

    def pop(self):
        if self.isEmpty():
            return -1
        self.__data.pop()

    def top(self):
        if self.isEmpty():
            return
        return self.__data[len(self.__data)-1]


    def isEmpty(self):
        return self.size() == 0

    def size(self):
        return len(self.__data)
