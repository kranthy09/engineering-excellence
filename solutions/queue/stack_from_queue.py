"""
Implement a stack using queue.

Stack:
- LIFO (Last In First Out) data structure

Queue:
- FIFO (First In First Out) data structure

Utilizing deque library from collections to implement stack.

Deque, (pronounced as "deck") is a double-ended queue structure:
- append(x): Add x to the right end of the deque.
- appendleft(x): Add x to the left end of the deque.
- pop(): Remove and return an element from the right end of the deque.
- popleft(): Remove and return an element from the left end of the deque.


"""
from collections import deque


class Stack:
    """
    Stack implementation using two deques

    q1: Represents main
    q2: Helper to handle push operation
    """

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        """
        TC: O(n)
        AS: O(1)
        """
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        """
        TC: O(1)
        AS: O(1)
        """
        if not self.q1:
            raise IndexError("Pop from empty stack")
        return self.q1.popleft()

    def top(self):
        """
        TC: O(1)
        AS: O(1)
        """
        if not self.q1:
            raise IndexError("Top from empty stack")
        return self.q1[0]


if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.top())  # Output: 3
    print(s.pop())  # Output: 3
    print(s.top())  # Output: 2
    print(s.pop())  # Output: 2
    print(s.top())  # Output: 1
    print(s.pop())  # Output: 1
    try:
        print(s.top())  # This will raise an error since the stack is empty
    except IndexError as e:
        print(e)
