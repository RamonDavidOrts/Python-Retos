class Queue:
    def __init__(self):
        self.__data = []

    def enqueue(self, element):
        self.__data.insert(0, element)

    def dequeue(self):
        if self.size() > 0:
            return self.__data.pop()
        raise Exception("Empty Queue")

    def front(self):
        if self.size() > 0:
            return self.__data[-1]
        raise Exception("Empty Queue")

    def rear(self):
        if self.size() > 0:
            return self.__data[0]
        raise Exception("Empty Queue")

    def size(self):
        return len(self.__data)

    def is_empty(self):
        return not self.__data

    def search(self, element):
        if element in self.__data:
            return self.__data.index(element)
        return -1

    def to_string(self):
        return str(self.__data)
