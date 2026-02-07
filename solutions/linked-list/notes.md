<!-- Source: week-9-[Arrays]/day-6-linkedlist -->

# Week 9 - Day 6

Date: January 31, 2026
Days since start: 69

## Notes

Linked List

## Practiced Problems

### 1. Insert an element at the begining of linked list

### 2. Print elements in linked list

### 3. Insert at the end

### 4. Insert at the position

### 5. Delete at the begining.

### 6. Delete at the end.

### 7. Delete at position

### 8. Reverse Linkedlist

### Pattern:

-

## Key Learnings

-

## Time Spent

- 1:
- 2:


---

<!-- Source: week-10/day-1-linked_list -->

# Week 10 - Day 1

Date: February 02, 2026
Days since start: 71

## Notes

Linked Lists
Linked list is a data structure to store in linking with the elements. An element in linked list is defined as Node, each node contains value and pointer, points to the next node. Link is established between one's node to another and have only one linking possible making it unidirectional.

Why Linkedlist:
Unlike array linked lists are not contingous in allocation, they can use any type of address in the memory and point to it's next node address. Lets us take 100 elements we have to store, but the memory have scattered of 4 bytes at one place, 10 bytes at another adress, 30 bytes at another part of the memory, where thay are not in contingous, here arrays has limitated and doesn't create the array of 100 contingous elements by raised memory fragmenetation. In that case, linked list are used to link between memory address in its own node by preserving the order of the elements should appear.

Declaration:
Linked lists are not built-in data structure, one should to be implement for their needs.
Here we consider a linkedlist of 5 elements and how they can be declarated

```
class LinkedList:
    def __init__(self, value, next_ = None):
        self.value = value
        self.next_ = next_

# define with values
ll = LinkedList(value=5, None) # pointing next value as null.

print(ll.value) # 5
print*ll.next_ # None.
```

Methods to implement in Linked List:

1. Insert an element at the begining of linked list
2. Print elements in linked list
3. Insert at the end
4. Insert at the position
5. Delete at the begining.
6. Delete at the end.
7. Delete at position
8. Reverse Linkedlist

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


---

<!-- Source: week-10/day-2-linkedlist -->

# Week 10 - Day 2

Date: February 03, 2026
Days since start: 72

## Notes

## Practiced Problems

### 1. Palindrome Reverse linkedlist approach

### 2.

### Pattern:

-

## Key Learnings

-

## Time Spent

- 1:
- 2:


---

<!-- Source: week-10/day-4-concept -->

# Week 10 - Day 4

Date: February 05, 2026
Days since start: 74

## Notes

## Practiced Problems

### 1. Clone LinkedList

### 2.

### Pattern:

-

## Key Learnings

-

## Time Spent

- 1:
- 2:
