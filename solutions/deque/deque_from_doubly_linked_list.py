"""
Implementation of Deque using Doubly Linked List in Python.

Deque is implemented using Doubly Linked List,
allows insertion and deletion at both ends in O(1) time complexity.

Each Node contains three parts:
- data: holds the value of the node
- prev: pointer to the previous node
- next: pointer to the next node

Operations:
- insert_front(x): Insert element at the front end of the deque.
- insert_rear(x): Insert element at the rear end of the deque.
- delete_front(): Remove and return the element from the front.
- delete_rear(): Remove and return the element from the rear.
- peek_front(): Return the element at the front.
- peek_rear(): Return the element at the rear.
- is_empty(): Check if the deque is empty.
- is_full(): Check if the deque is full (applicable for fixed-size deques).
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


class DequeFromDLL(Generic[T]):
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

    def insert_front(self, x: T) -> None:
        """
        Insert at the front of the deque.
        """
        # Implementation of insert_front method
        if self._size == self.cap:
            raise IndexError("Insert on Full Deque")
        data_node = Node(x)
        if self._size == 0:
            self.head = self.tail = data_node
        else:
            data_node.next = self.head
            self.head.prev = data_node
            self.head = data_node
        self._size += 1

    def insert_rear(self, x: T) -> None:
        """
        Insert at the rear end of the deque
        """
        if self._size == self.cap:
            raise IndexError("Insert on Full Queue")
        data_node = Node(x)
        if self._size == 0:
            self.head = self.tail = data_node
        else:
            self.tail.next = data_node
            data_node.prev = self.tail
            self.tail = data_node
        self._size += 1

    def delete_front(self) -> T:
        """
        Delete and return front of the Deque
        """
        if self._size == 0:
            raise IndexError("Delete on Empty Queue")
        val = self.head.value
        if self._size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self._size -= 1

        return val

    def delete_rear(self) -> T:
        """
        Delete and return rear of the Deque
        """
        if self._size == 0:
            raise IndexError("Delete on empty Queue")
        val = self.tail.value
        if self._size == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self._size -= 1
        return val

    def peek_front(self) -> T:
        """
        Return the front element without removing it.
        """
        if self._size == 0:
            raise IndexError("Front from Empty Queue")
        return self.head.value

    def peek_rear(self) -> T:
        """
        Return the rear element without removing it.
        """
        if self._size == 0:
            raise IndexError("Rear from Empty Queue")
        return self.tail.value

    def is_empty(self) -> bool:
        """
        Check if the deque is empty.
        """
        return self._size == 0

    def is_full(self) -> bool:
        """
        Check if the deque is full (applicable for fixed-size deques).
        """
        return self._size == self.cap

    def size(self) -> int:
        """
        Return the number of elements in the deque.
        """
        return self._size

    def __repr__(self) -> str:
        """
        String representation of the deque for debugging purposes.
        """
        elements = []
        current = self.head
        while current:
            elements.append(repr(current.value))
            current = current.next
        return "DequeFromDLL([" + ", ".join(elements) + "])"


if __name__ == "__main__":
    # Example usage of DequeFromDLL
    deque = DequeFromDLL[int](5)
    deque.insert_rear(1)
    deque.insert_rear(2)
    deque.insert_front(0)
    print(deque)  # DequeFromDLL([0, 1, 2])
    print(deque.delete_front())  # 0
    print(deque.delete_rear())   # 2
    print(deque.peek_front())    # 1
    print(deque.peek_rear())     # 1
    print(deque.is_empty())      # False
    print(deque.is_full())       # False
    print(deque.size())          # 1
