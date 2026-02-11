"""
Reversing a Queue

Implemented using a Stack, such that, utilizing the LIFO
property of stack to reverse the order of elements in the queue.

Approach:
1. Deque all elements from the queue and push them onto stack.
2. Pop all elements from stack and enque them back to the queue.

TC: O(n)
AS: O(n) for stack
"""

from typing import Generic, TypeVar

T = TypeVar('T')  # Generic type variable


class Stack(Generic[T]):
    """
    Stack implementation using list
    """

    def __init__(self, capacity: int):
        self.stack: list = []
        self._size: int = 0
        self.cap: int = capacity

    def push(self, x: T) -> None:
        """
        Insert element on top of stack
        """
        if self._size == self.cap:
            raise OverflowError("Stack is Full")
        self.stack.append(x)
        self._size += 1

    def pop(self) -> T:
        """
        Remove and return the top element of the stack
        """
        if self._size == 0:
            raise IndexError("Pop from Empty Stack")
        self._size -= 1
        return self.stack.pop()

    def top(self) -> T:
        """
        Return the top element of the stack without removing it
        """
        if self._size == 0:
            raise IndexError("Top from Empty Stack")
        return self.stack[-1]


class Queue(Generic[T]):
    """
    Queue implementation using list
    """

    def __init__(self, capacity: int):
        self.queue: list = []
        self._size: int = 0
        self.cap: int = capacity

    def enque(self, x: T) -> None:
        """
        Insert element at the rear end of the queue
        """
        if self._size == self.cap:
            raise OverflowError("Queue is Full")
        self.queue.append(x)
        self._size += 1

    def deque(self) -> T:
        """
        Remove and return the front element of the queue
        """
        if self._size == 0:
            raise IndexError("Dequeue from Empty Queue")
        self._size -= 1
        return self.queue.pop(0)

    def __repr__(self):
        """
        String representation of the queue
        """
        return str(self.queue)


def reverse_queue(q: Queue[T]) -> None:
    """
    TC: O(n)
    AS: O(n) for stack
    """
    stack = Stack[T](q.cap)
    # Deque all elements from the queue and push them onto stack
    while q._size > 0:
        stack.push(q.deque())
    # Pop all elements from stack and enque them back to the queue
    while stack._size > 0:
        q.enque(stack.pop())


if __name__ == "__main__":
    q = Queue[int](10)
    q.enque(1)
    q.enque(2)
    q.enque(3)
    q.enque(4)
    print("Original Queue:", q.queue)  # Output: [1, 2, 3, 4]
    reverse_queue(q)
    print("Reversed Queue:", q.queue)  # Output: [4, 3, 2, 1]
