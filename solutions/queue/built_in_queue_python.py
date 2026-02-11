"""
Implementation of Deque data structure in python

- Python also has a dedicated queue module.
  (e.g., queue.Queue, queue.LifoQueue, queue.PriorityQueue).

- In fact, the queue.Queue class uses collections.deque
  internally for its data storage.

- In Python collections module provides a built-in implementation
  of a double-ended queue, called `deque`.

Deque is implemented using Doubly Linked List,
allows insertion and deletion at both ends in O(1) time complexity.

Each Node contains three parts:
- data: holds the value of the node
- prev: pointer to the previous node
- next: pointer to the next node

Operations:
- euque(x): Insert element at the rear end of the deque.
- deque(): Remove and return the element from the front end of the deque.
- peek_front(): Return the front element without removing it.
- peek_rear(): Return the rear element without removing it.
- isEmpty(): Check if the deque is empty.
- isFull(): Check if the deque is full (applicable for fixed-size deques).
- size(): Return the number of elements in the deque.
- __repr__(): String representation of the deque for debugging purposes.
"""

from typing import Generic, Optional, TypeVar


T = TypeVar('T')  # Generic type variable


class Node(Generic[T]):
    """
    Node class for doubly linked list
     - value: holds the data
     - prev: pointer to the previous node
     - next: pointer to the next node
     """

    def __init__(self, value: T):
        self.value = value
        self.prev: Optional[Node[T]] = None
        self.next: Optional[Node[T]] = None


class DequeDLL(Generic[T]):
    """
    Deque implementation using doubly linked list

    - front: pointer to the front node
    - rear: pointer to the rear node
    - cap: maximum capacity of the deque
    - _size: current number of elements in the deque
    """

    def __init__(self, capacity: int):
        self.head: Optional[Node[T]] = None
        self.tail: Optional[Node[T]] = None
        self.cap = capacity
        self._size = 0

    def enque(self, x: T) -> None:
        """
        Insert at the rear end of the deque.
        """
        # Implementation of enque method
        # base case
        data_node = Node(x)
        if self.tail is None:
            self.head = self.tail = data_node
        else:
            self.tail.next = data_node
            data_node.prev = self.tail
            self.tail = data_node
        self._size += 1

    def deque(self) -> T:
        """
        Remove and return the element from the front end of the deque.
        """
        # Implementation of deque method
        # base case
        if self.head is None:
            raise IndexError("Remove from Empty Queue")
        else:
            val = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        self._size -= 1
        return val

    def peek_front(self) -> T:
        """
        Return the front element without removing it.
        """
        # Implementation of peek_front method
        # base case
        if self.head is None:
            raise IndexError("Front from Empty Queue")

        return self.head.value

    def peek_rear(self) -> T:
        """
        Return the rear element without removing it.
        """
        # Implementation of peek_rear method

        # base case
        if self.tail is None:
            raise IndexError("Rear from Empty Queue")

        return self.tail.value

    def is_full(self) -> bool:
        """
        Check if the deque is full (applicable for fixed-size deques).
        """
        # Implementation of is_full method
        return self._size == self.cap

    def is_empty(self) -> bool:
        """
        Check if the deque is empty.
        """
        # Implementation of is_empty method
        return self._size == 0

    def size(self) -> int:
        """
        Return the number of elements in the deque.
        """
        # Implementation of size method
        return self._size

    def __repr__(self):
        """
        String representation of the deque for debugging purposes.
        """
        values = []
        current = self.head
        while current:
            values.append(repr(current.value))
            current = current.next
        return "DequeDLL([" + ", ".join(values) + "])"


if __name__ == "__main__":
    d = DequeDLL[int](5)
    d.enque(1)
    d.enque(2)
    d.enque(3)
    print(d.peek_front())  # Output: 1
    print(d.peek_rear())   # Output: 3
    print(d.deque())       # Output: 1
    print(d.size())        # Output: 2
    print(d.is_empty())    # Output: False
    print(d.is_full())     # Output: False
    d.enque(4)
    d.enque(5)
    print(d.is_full())     # Output: True
    print(d)              # Output: DequeDLL([2, 3, 4, 5])
