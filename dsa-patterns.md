# DSA Pattern Library

**Purpose:** This is your pattern recognition engine. After solving each problem, add the pattern trigger here.

---

## Pattern 1: Two Pointers

### When to Use (Recognition Triggers)

- Array/string is **sorted** or can be sorted
- Looking for **pair/triplet** that satisfies a condition
- Need to **compare elements from both ends**
- Problems with words: "pair", "closest", "minimum difference"

### Core Technique

```python
def two_pointers_template(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Check condition
        # Move pointers based on condition
        # left += 1 or right -= 1

    return result
```

### Problems Solved

1. [Problem name] - [Key insight from your solution]
2. [To be added as you practice]

### Common Mistakes I Made

- [Add after solving problems]

### Optimization Insight

- Time: O(n), Space: O(1) typically

---

## Pattern 2: Sliding Window

### When to Use (Recognition Triggers)

- **Subarray/substring** problems
- Words: "contiguous", "window", "consecutive"
- Find **maximum/minimum in range**
- **K elements** constraint

### Core Technique

```python
def sliding_window_template(arr, k):
    window_start = 0
    window_sum = 0
    max_sum = float('-inf')

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # Expand window

        if window_end >= k - 1:  # Window size reached
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]  # Shrink window
            window_start += 1

    return max_sum
```

### Problems Solved

1. [To be added]

### When NOT to Use

- Elements aren't contiguous
- Need to consider all subarrays (might need DP)

---

## Pattern 3: Hash Map for Frequency/Lookup

### When to Use (Recognition Triggers)

- Need **O(1) lookup**
- Count **frequency** of elements
- Find **complement** (like Two Sum)
- Check **existence** quickly

### Core Technique

```python
def hash_map_template(arr, target):
    seen = {}  # or defaultdict, Counter

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []
```

### Problems Solved

1. [To be added]

---

## Pattern Template (Copy for New Patterns)

### When to Use (Recognition Triggers)

-

### Core Technique

```python
# Template code
```

### Problems Solved

1.

### Common Mistakes I Made

-

### Time/Space Complexity

- ***

## My Pattern Recognition Checklist

**Before coding, ask:**

1. Is the data sorted? → Two Pointers, Binary Search
2. Need subarray/substring? → Sliding Window
3. Need fast lookup/frequency? → Hash Map
4. Tree problem? → Think DFS/BFS first
5. Optimization problem? → Might be DP
6. Graph connectivity? → Union Find or DFS

**After solving, ask:**

1. What was the trigger I missed initially?
2. Could I have recognized this pattern in 2 minutes?
3. What similar problem would use this pattern?
