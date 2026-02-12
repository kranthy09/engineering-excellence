"""
Implement Deque using circular array.

Considering list as circular array, by changing the front and rear
pointers to enque and deque elements and change their positions.

So, we start front pointer with 0 and rear pointer at -1, telling
rear pointer moves in circular manner and reaches front of the array.

Operations:
- insertFront(): Adds an item at the front of Deque.
- insertLast(): Adds an item at the rear of Deque.
- deleteFront(): Deletes an item from the front of Deque.
- deleteLast(): Deletes an item from the rear of Deque.

TC: O(1) for all operations.
AS: O(n) for circular array implementation.
"""

from typing import List, TypeVar

T = TypeVar('T')  # Generic type variable


class DequeCircularArray:
    """
    Deque implementation using circular array

    - arr: list to hold the elements of the deque
    - front: index of the front element
    - rear: index of the rear element
    - cap: maximum capacity of the deque
    - _size: current number of elements in the deque
    """

    def __init__(self, capacity: int):
        self.arr: List[T] = [None] * capacity  # Initialize the array with None
        self.front = 0  # Front index
        self.rear = -1  # Rear index
        self.cap = capacity  # Maximum capacity
        self._size = 0  # Current size of the deque

    def insertFront(self, x):
        """
        Add element at the front.
        """
        if self._size == self.cap:
            raise Exception("Deque is full")
        if self._size == 0:
            self.front = self.rear = 0
        else:
            self.front = (self.front + self.cap - 1) % self.cap
        self.arr[self.front] = x
        self._size += 1

    def insertRear(self, x):
        """
        Adds an element at the rear.
        """
        if self._size == self.cap:
            raise IndexError("Insert on Full Deque")
        if self._size == 0:
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.cap
        self.arr[self.rear] = x
        self._size += 1

    def deleteFront(self):
        """
        Deletes and returns an element at the Front
        """
        if self._size == 0:
            raise IndexError("Delete on Empty Deque")
        val = self.arr[self.front]
        self.arr[self.front] = None

        if self._size == 1:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.cap

        self._size -= 1
        return val

    def deleteRear(self):
        """
        Delete an element at the rear.
        """
        if self._size == 0:
            raise IndexError("Delete on Empty Deque")
        val = self.arr[self.rear]
        self.arr[self.rear] = None
        if self._size == 1:
            self.front = self.rear = -1
        else:
            self.rear = (self.rear + self.cap - 1) % self.cap
            self._size -= 1

        return val

    def peekFront(self):
        """
        Get the front item from the deque.
        """
        if self._size == 0:
            raise IndexError("Peek on Empty Deque")
        return self.arr[self.front]

    def peekRear(self):
        """
        Get the last item from the deque.
        """
        if self._size == 0:
            raise IndexError("Peek on Empty Deque")
        return self.arr[self.rear]

    def isEmpty(self):
        """
        Check whether the circular deque is empty or not.
        """
        return self._size == 0

    def isFull(self):
        """
        Check whether the circular deque is full or not.
        """
        return self._size == self.cap

    def size(self):
        """
        Return the number of elements in the deque.
        """
        return self._size

    def __repr__(self):
        """
        String representation of the deque.
        """
        if self._size == 0:
            return "Deque is empty"
        elements = []
        for i in range(self._size):
            index = (self.front + i) % self.cap
            elements.append(str(self.arr[index]))
        return "Deque: " + " <- ".join(elements)


if __name__ == "__main__":
    deque = DequeCircularArray(5)
    deque.insertRear(1)
    deque.insertRear(2)
    deque.insertFront(3)
    print(deque.arr)  # [1, 2, None, None, 3]
    deque.insertFront(4)
    deque.deleteFront()
    deque.deleteRear()
    print(deque.arr)  # [1, None, None, None, 3]
    print(deque.peekFront())  # Output: 3
    print(deque.peekRear())   # Output: 1
    print(deque.isEmpty())    # Output: False
    print(deque.isFull())     # Output: False
    print(deque.size())       # Output: 2
    print(deque)             # Deque: 3 <- 1
