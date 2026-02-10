# Week 10 - Day 7

Date: February 08, 2026
Days since start: 77

# Notes

Doublly Linkedlist Problem: Remove Duplicates in doubly linkedlist.

Stacks:

LIFO: Last in first Out
Random access is not possible. Only the top element is accessible.

Major Operation:

1. Push
2. Pop
3. Peek to Top
4. size
5. is empty

Stack is not a primitive data structure, it can implemented.
We can implement stack with array or linked list.
With array:

```python


class Stack:
    def __init__(self):
        self.arr = []
        self.size_ = 0

    def push(self, data):
        self.arr.append(data)
        sef.size += 1

    def pop(self):
        self.arr.pop()
        self.size -= 1

    def top(self):
        return self.arr[-1]

    def size(self):
        return self.size_

    def is_empty(self):
        return self.size_ <= 0


```

Implement stack using LinkedList

```python


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = head


class Stack:
    def __init__(self):
        self.head = head
        self._size = 0

    def push(self, data):
        data_node = Node(data)
        data_node.next = self.head
        self.head = data_node


```

Problem solving on Stacks:

1. Check if the paranthesis are in order.

# Practiced Problems

# 1. Remove Duplicates in doubly linkedlist.

# 2. Check if the paranthesis are in order.
