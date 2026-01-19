# Week 0 - Day 5

Date: November 29, 2025
Days since start: 5

## Problems

1.Longest Substring Without Repeating Characters (Medium)

2.

## Pattern:

Substring should be tracked with left and right (two pointers)
the right pointer waits for left to remove characters that doesnot
meet unique condition.

-> take the right pointer char
-> append the char
-> if the char is already in hashset, move left until it exludes char in hashset

## Key Learnings

The ability to give a pointer to stop for removing duplicates
that points to left which is the start of the next substring

## Time Spent

- Problem 1: 1h 30m
- Problem 2:
