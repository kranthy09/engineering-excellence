# Week 11 - Day 4

Date: February 12, 2026
Days since start: 81

## Notes

### Deque: Double Ended Queue

- Deque is a data structure that allows insertion and deletion of elements from both ends.
- It can be implemented using a circular array or a doubly linked list.
- Common operations include:
  - `push_front`: Add an element to the front of the deque.
  - `push_back`: Add an element to the back of the deque.
  - `pop_front`: Remove an element from the front of the deque.
  - `pop_back`: Remove an element from the back of the deque.
  - `front`: Get the front element of the deque.
  - `back`: Get the back element of the deque.

  Time Complexity:
  - All operations (push_front, push_back, pop_front, pop_back, front, back) can be performed in O(1) time.

#### Variations of Deque:

- Circular Deque: A deque that is implemented using a circular array, allowing for efficient use of space.
- Priority Deque: A deque that allows for elements to be added with a priority, where higher priority elements are removed before lower priority ones.
- Bounded Deque: A deque that has a fixed size, and cannot grow beyond that size.
- Unbounded Deque: A deque that can grow indefinitely as elements are added.

## Deque implementations from Circular Array and Doubly Linked List:

### from Circular Array:

Implement Deque using List.

Operations:

- insert_front(x): Insert element at the front end of the deque.
- insert_rear(x): Insert element at the rear end of the deque.
- delete_front(): Remove and return the element from the front end of the deque.
- delete_rear(): Remove and return the element from the rear end of the deque.
- peek_front(): Return the element at the front.
- peek_rear(): Return the element at the rear.
- is_full(): Return true if the deque is full, false otherwise.
- is_empty(): Return true if the deque is empty, false otherwise.

All the operations should be performed in O(1) time complexity.

How can a list be O(1) for all operations?

If we apply a deque() operation on list, it will take O(n) time to shift all elements to the left.
So, we can maintain two pointers, front and rear, to keep track of the front and rear of the deque.
When we enque an element, we can add it to the rear and move the rear pointer to the next position.
When we deque an element, we can remove it from the front and move the front pointer to the next position.
This way, we can achieve O(1) time complexity for all operations.

How can we remove an element and move the front pointer in O(1) time?, We can maintain a circular array to implement the deque.
When we enque an element, we can add it to the rear and move the rear pointer to the next position (modulo the capacity).
When we deque an element, we can remove it from the front and move the front pointer to the next position (modulo the capacity).

Means, deque implementation is possible with circular array, not with a simple list.
A simple list will require O(n) time for deque operation due to shifting of elements.

## Deque from Doubly Linked List:

Implement Deque using Linked List.

In singly linked list, we can insert an element at front and rear in O(1) time, but we cannot delete an element from rear in O(1) time as we need to traverse the list to find the second last element.

So we can use a doubly linked list to implement the deque, where the insertions and deletions can be done in O(1) time from both ends.

Operations:

- insert_front(x): Insert element at the front end of the deque.
- insert_rear(x): Insert element at the rear end of the deque.
- delete_front(): Remove and return the element from the front end of the deque.
- delete_rear(): Remove and return the element from the rear end of the deque.
- peek_front(): Return the element at the front.
- peek_rear(): Return the element at the rear.
- is_empty(): Return true if the deque is empty, false otherwise.

## Practiced Problems

### 1.

### 2.

### Pattern:

-

## Key Learnings

-

## Time Spent

- 1:
- 2:
