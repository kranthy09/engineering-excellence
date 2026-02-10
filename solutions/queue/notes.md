# Week 11 - Day 2

Date: February 10, 2026
Days since start: 79

## Notes

### Queue Data Structure

It works with the rule, First In First Out(FIFO).

#### Operations on Queue:

- _Enqueue_: Insert element at the end of the queue

- _Dequeue_: Remove element from the front of the queue
- _Peek_: Get the front element of the queue without removing it.
- _Size_: Get the number of elements in the queue.
- _IsEmpty_: Check if the queue is empty.
- _IsFull_: Check if the queue is full (applicable for fixed-size queues).
- _getRear_: Get the rear element of the queue without removing it.
- _getFront_: Get the front element of the queue without removing it.

Queues can be implemented using arrays or linked lists. In an array-based implementation, we can use a circular array to efficiently utilize space. In a linked list-based implementation, we can maintain pointers to the front and rear of the queue for efficient enqueue and dequeue operations.

### Applications of Queues:

- Single source and multiple consumers, such as in ticketing systems, where customers line up to purchase tickets.
- Task scheduling, where tasks are queued for execution. FCFS (First Come First Serve) scheduling is a common example of this.
- Sync between two processes, where one can be slow and the other can be fast. The queue helps in managing the flow of data between them.
- Computer networks, where queues are used to manage data packets in routers and switches.

### Variations:

- Circular Queue: A circular queue is a linear data structure that follows the FIFO principle but connects the end of the queue back to the front, forming a circle. This allows for efficient use of space and avoids the need for shifting elements when enqueuing or dequeuing.
- Deque (Double-Ended Queue): A deque is a generalized version of a queue that allows insertion and deletion at both ends. It can be used as both a stack and a queue, providing more flexibility in data management.
- Priority Queue: A priority queue is a special type of queue where each element is associated with a priority. Elements with higher priority are dequeued before those with lower priority, regardless of their order in the queue.
- Doubly ended priority queue: A double-ended priority queue is a data structure that allows for the insertion and deletion of elements based on their priority, similar to a priority queue. However, it also allows for the retrieval of both the highest and lowest priority elements efficiently. This can be useful in scenarios where you need to manage tasks or resources with varying levels of importance.

## Practiced Problems

### 1. Implement a queue using array

### 2. Implement a queue using circular array

### Pattern:

- Straight forward implementation of queue using array and circular array.

## Key Learnings

- Understanding the significance of modulo operation in circular queue to maintain elements in cirucular manner.
- Recognizing the advantages of circular queues in terms of space efficiency compared to linear queues.

## Time Spent

- 1: Implement a queue using array - 20 mins
- 2: Implement a queue using circular array - 30 mins
