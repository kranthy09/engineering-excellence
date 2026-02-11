"""
Linked List implementation of Queue

"""

from typing import Optional, TypeVar, Generic

T = TypeVar('T')  # Generic type variable


class Node(Generic[T]):
    """
    Node class for linked list
     - value: holds the data
     - next: pointer to the next node

    - Generic type T allows for any data type to be stored in the node
    """

    def __init__(self, value: T):
        self.value = value
        self.next: Optional[Node[T]] = None


class LinkedListQueue(Generic[T]):
    """
    Queue implementation using linked list
    """

    def __init__(self, capacity: int):
        self.front: Optional[Node[T]] = None
        self.rear: Optional[Node[T]] = None
        self.cap = capacity
        self._size = 0

    def enque(self, x: T) -> None:
        """
        Insert at the end
        """
        if self._size == self.cap:
            raise OverflowError("Queue is Full")
        new_node = Node(x)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def deque(self) -> T:
        """
        Remove from front
        """
        if self._size == 0:
            raise IndexError("Queue is Empty")
        val = self.front.value
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
        self._size -= 1
        return val

    def size(self) -> int:
        """
        Return size of queue
        """
        return self._size

    def peek_front(self) -> T:
        """
        Returns front element
        """
        if self._size == 0:
            raise IndexError("Queue is Empty")
        return self.front.value

    def peek_rear(self) -> T:
        """
        Returns rear element
        """
        if self._size == 0:
            raise IndexError("Queue is Empty")
        return self.rear.value

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

    def __repr__(self):
        """
        String representation of the queue
        """
        elements = []
        current = self.front
        while current:
            elements.append(str(current.value))
            current = current.next
        return " -> ".join(elements)


if __name__ == "__main__":
    q = LinkedListQueue[int](5)
    q.enque(1)
    q.enque(2)
    q.enque(3)
    q.enque(4)
    q.enque(5)
    print("Queue: ", q)
    print("Front element: ", q.peek_front())
    print("Rear element: ", q.peek_rear())
    print("Queue size: ", q.size())
    print("Dequeue element: ", q.deque())
    print("Front element after dequeue: ", q.peek_front())
    print("Is queue empty? ", q.is_empty())
    print("Is queue full? ", q.is_full())
