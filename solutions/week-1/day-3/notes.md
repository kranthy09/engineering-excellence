# Week 1 - Day 3

Date: December 03, 2025
Days since start: 10

## Problems

1. Boats to Save People (Medium)
   You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.
   Return the minimum number of boats to carry every given person.

## Pattern:

#### Ask Questions:

- do we have order in the array?
  : No, but ordering might help
- if the max weight of persons is greater than limit?
  : solution not found case.

#### Visualization:

- At any time we have two choices, take one person or take both persons, and which person is take from both. if we can send the lightest person with heavier can help to maintain the least boats used. so sorting the data can help us to identify which person can pick.

**Two pointers Pattern** , at start and end positions moves inwards to select one or two persons and greater weights pointer moving inward, such that current lighter person is again checked with next larger person.

at an instance of allocating the persons to boats, at start, end indices,

```python
if nums[start] + nums[end] <= limit:
    boats_count += 1
    start += 1
    end -= 1
else:
    boats_count += 1
    end -= 1
```

## Key Learnings

- Identification of pattern and solution in visualization step.
- Order in array elements can help find the pairs efficiently.
- Used "which choices to make" thinking from recursion solving technique.s

## Time Spent

- Problem 1:
- Problem 2:
