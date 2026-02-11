"""
Implementation of Static Queue using Array

"""


class Queue:

    def __init__(self, n):
        self.arr = []
        self.cap = n
        self._size = 0

    def enque(self, x):
        """
        Insert at the end
        """
        if self._size == self.cap:
            print("Capacity full")
        self.arr.append(x)
        self._size += 1

    def deque(self):
        """
        Remove at the begining
        """
        if self._size == 0:
            return "Empty queue"
        if self._size == 1:
            self._size -= 1
            return self.arr.pop()
        res = self.arr[0]

        for i in range(self._size - 1):
            self.arr[i] = self.arr[i+1]
        self.arr = self.arr[:-1]
        self._size -= 1
        return res

    def getFront(self):
        """
        Return Queue front
        """
        if self._size > 0:
            return self.arr[0]
        return "Empty Queue"

    def getRear(self):
        """
        Return Queue rear
        """
        if self._size > 0:
            return self.arr[-1]
        return "Empty Queue"

    def isFull(self):
        """
        Return True if size is cap
        """
        return self._size == self.cap

    def isEmpty(self):
        """
        Returns True if size is 0
        """
        return self._size == 0

    def size(self):
        """
        return size of Queue
        """
        return self._size


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    q = Queue(n)
    for element in arr:
        q.enque(element)
    print(q.arr)
    q.deque()
    print(q.arr)
    print(q.getFront())
    print(q.getRear())
    print(q.isFull())
    print(q.isEmpty())
    print(q.size())
