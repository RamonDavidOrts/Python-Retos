class Stack:
    def __init__(self):
        self.__data = []

    def push(self, element):
        self.__data.append(element)

    def pop(self):
        if self.size() > 0:
            return self.__data.pop()
        raise Exception("Empty Stack")

    def top(self):
        if self.size() > 0:
            return self.__data[-1]
        raise Exception("Empty Stack")

    def peek(self):
        return self.top()

    def size(self):
        return len(self.__data)

    def empty(self):
        return not self.__data

    def search(self, element):
        if element in self.__data:
            return self.__data.index(element)
        return -1

    def to_string(self):
        return str(self.__data)
