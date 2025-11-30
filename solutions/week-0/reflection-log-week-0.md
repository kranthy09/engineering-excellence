# Week 0 Review

**Date Range:** [Start Date] - [End Date]
**Review Date:** November 30, 2025

---

## Problems Solved This Week

| Day | Problem 1                                 | Problem 2 | Pattern      | Time   | First Try? |
| --- | ----------------------------------------- | --------- | ------------ | ------ | ---------- |
| 1   | container with most water                 | -         | Two pointers | 1h 30m | ❌         |
| 2   | Trapping rain water                       | -         | Two pointers | 2h     | ❌         |
| 3   | Remove duplicated from sorted array       | -         | Two pointers | 2h     | ❌         |
| 4   | Sort colors                               | -         | Two pointers | 1h 30m | ❌         |
| 5   | Longest substring without repeating chars | -         | Two pointers | 1h 30m | ❌         |
| 6   | -                                         | -         | -            | -      | ✅/⚠️/❌   |
| 7   | -                                         | -         | -            | -      | ✅/⚠️/❌   |

**Total Problems:** 5
**Success Rate (First Try):** 0
**Average Time (Medium):** 1h 30m

---

## Patterns Progress

### Mastered ✅

-

### Practicing 🔄

Two pointers

### Not Started ⏳

- ***

## Key Learnings

### Pattern Recognition

Two pointers is such that they are moved with respect to the condition, one can represent an element, other can represent the position it is moving, based on the problem, the two pointers are moved in such way to acheive the solution to the problem.

#### Problem 1:

Container with most water:
How the problem should be deduced to two pointers, walls represent the two pointers, here straight forward. So we have to move two pointers in the given array such that the water between those two pointers should have most water.

Intuition: contianer with tall height will store more water.
We will come from the brute force approach, what we do in brute force. We will find all the possiblities of the container that are formed and calculate the area of water contain and return the max two indices and with most water contain.

making this some smartness over here, instead of looping for each element of i pair with each element of j from starting, consider first and last pointers that pointed to first and last elements in the array.
so that they are compared and the two pointers are moved in such way that they contain most water.
consider the situation, if the height of left is greater that right, the more water can stored with higher height, so we move right pointer inward to compensate the width. As we are finding maximum so we concentrate on what matters.

so the pattern looks like this,
first and last at 0, n-1
compares the height for first, last and one pointer moves inward.
until the left pointer is smaller than right.

### New Concepts

-one pointer is moved with a condition, inward up to they both cross each other.

- Everything comes from visualization, if we can visualize the problem into runnable animation inside the brain do it with clean thought on paper so improve problem understanding, we have to identify by visualizing the pattern.

### Debugging Insights

- print statements with clear on paper debugging helps to understand the code for improvements.

## Communication Improvements

### What Worked Well

-

### What to Improve

-

### Clarity Score

- Start of week: \4\_/10
- End of week: \8\_/10

---

## Freeze Moments

### When Did I Freeze?

- How the two pointers are applied to this current problem, how they are being moved on what condition?

### Why?

- Practice with full clarity on paper to observe the pattern how they are being used.
- Should practice it loudly.

### How to Prevent Next Time?

- Every thought will be put on paper or speak out loudly

## Best Moment This Week

**Problem:**
**Why:**

Understanding this patterns animatedly then observing their patterns is the moment of the week.

## Biggest Challenge

**Problem:**
**What Made It Hard:**
**How I Overcame It:**

Try to complete 2 problems in a day.

## Meta-Learning

_What did I learn about HOW I learn?_

- I learned how patterns are recogine, it is obtained with behavoiur of the problem statement that can transformed to a continous pattern so that it can be coded for the solution.
- So analysing patterns with the help of pen and paper practice and visualizing it can help determine the solution.

## Next Week Focus

- Two pointer, with solving 2 problems a day, concentrate on time complexity, give worst case and best case scenarios.
- Explore about communication in interview context.

### Pattern to Master

- Two pointers, sliding window

### Communication Goal

- Know how an interview is conducted and what should be said in the process?

### Mindset Shift

- From this looks difficult i am getting freeze to try to visualize the given problem, trying to build the logic.

## Statistics

- **Total problems solved:** 5
- **Patterns learned:** 1
- **Time spent coding:** 7h 30m
- **Mock interviews:** 0

---

## Evidence of Progress

_Compare to previous weeks - what improved?_

- Structurized thinking with clear process to solve the problem.
