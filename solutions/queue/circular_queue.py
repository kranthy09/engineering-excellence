"""
Implementing Circular Queue using Array
Efficient implementation of Queue using Array

Time Complexity: O(1) for enque and deque
"""

from typing import TypeVar, Generic, Optional, List


T = TypeVar('T')  # Generic type variable


class CircularQueue(Generic[T]):
    """
    Circular Queue using array indexing

    Why circular?
    - Reuses space by wrapping around
    - Dequeue is O(1), just move front pointer
    - No shifting elements
    - Front and rear pointers track elements
    """

    def __init__(self, capacity: int):
        self.arr: List[Optional[T]] = [None] * capacity
        self.cap = capacity
        self.front = 0
        self.rear = -1
        self._size = 0

    def enque(self, x: T) -> None:
        """
        Insert
        """
        if self._size == self.cap:
            raise OverflowError("Queue is Full")
        self.rear = (self.rear + 1) % self.cap
        self.arr[self.rear] = x
        self._size += 1

    def deque(self) -> T:
        """
        Remove from front
        """
        if self._size == 0:
            raise IndexError("Queue is Empty")
        val = self.arr[self.front]
        self.front = (self.front + 1) % self.cap
        self._size -= 1
        return val

    def peek_front(self) -> T:
        """
        Returns Front
        """
        if self._size == 0:
            raise IndexError("Queue is Empty")
        return self.arr[self.front]

    def peek_rear(self):
        """
        Returns Rear
        """
        if self._size == 0:
            raise IndexError("Queue is Empty")
        return self.arr[self.rear]

    def is_full(self) -> bool:
        """
        Returns True if size is cap
        """
        return self._size == self.cap

    def is_empty(self) -> bool:
        """
        Returns True if size is 0
        """
        return self._size == 0

    def __len__(self) -> int:
        """
        Returns size of queue
        """
        return self._size

    def __repr__(self):
        if self._size == 0:
            return "CircularQueue([])"
        elements = []
        for i in range(self._size):
            index = (self.front + i) % self.cap
            elements.append(self.arr[index])
        return f"CircularQueue({elements})"


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    cq = CircularQueue[int](n)
    for element in arr:
        cq.enque(element)
    print(cq)
    print("Dequeued:", cq.deque())
    print(cq)
    print("Front:", cq.peek_front())
    print("Rear:", cq.peek_rear())
    print("Is Full?", cq.is_full())
    print("Is Empty?", cq.is_empty())
    cq.enque(6)  # This will raise OverflowError
