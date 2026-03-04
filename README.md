# Engineering Excellence — DSA Solutions

> A structured, progressively built collection of Data Structures & Algorithms solutions — written with clarity, documented with intent, and tracked in real time.

**Live metrics & progress dashboard → [evolune.dev/dsa](https://evolune.dev/dsa)**

---

## What This Repository Is

This is a personal DSA practice repository built around one principle: **understand the pattern, not just the solution.**

Every problem here is approached at least twice — first with a brute-force solution to establish correctness, then refined toward an optimal approach. Each file is self-contained: problem statement, multiple implementations, time/space complexity analysis, and runnable test cases — all in one place.

This repo is synced live to [evolune.dev/dsa](https://evolune.dev/dsa). Every commit triggers a backend sync, so the page always reflects the current state of this work.

---

## Topics Covered

| Category               | Focus Areas                                                               |
| ---------------------- | ------------------------------------------------------------------------- |
| **Arrays**             | Subarrays, rotation, leaders, prefix sums, matrix operations              |
| **POTD**               | Mixed problems — inversions, XOR, H-index, chocolate distribution         |
| **Recursion**          | Permutations, combinations, N-Queens, Sudoku solver, maze problems        |
| **Binary Trees**       | Traversals, views (top/left/right), level order, height, K-distance nodes |
| **Linked Lists**       | Reverse, palindrome, loop detection, clone with random pointers, merging  |
| **Queue**              | Circular queue, first non-repeating stream, deque-based sliding max       |
| **Mathematics**        | Power functions, digit counting, nCr, string multiplication               |
| **Bit Magic**          | Set/unset/toggle bits, XOR tricks, Sieve of Eratosthenes                  |
| **Matrix**             | Rotation, transpose, spiral traversal, search in sorted matrix            |
| **Two Pointers**       | 3-sum, 4-sum, container with most water, longest subarray patterns        |
| **Deque**              | Min/max structures, circular array problems, sliding window maximum       |
| **Stacks**             | Parenthesis matching, next greater element, max of minimums               |
| **Doubly Linked List** | Insert, remove duplicates, add numbers                                    |
| **Sliding Window**     | Advanced substring concatenation patterns                                 |

Theory notes and complexity analysis are documented alongside each topic.

---

## Solution Format

Every solution file follows a consistent structure:

```python
"""
Problem Name (Difficulty)
@topic: category
@difficulty: easy / medium / hard
@tags: relevant_tags

Problem statement with examples
i/p: ...
o/p: ...

Approaches:
1. Brute Force — description
2. Optimal — description
"""

class Solution:
    def brute_force(self, ...):
        """TC: O(n²)  AS: O(1)"""
        ...

    def optimal(self, ...):
        """TC: O(n)  AS: O(1)"""
        ...

if __name__ == "__main__":
    # Runnable test cases
```

This format makes it easy to trace the thinking process — from the naive solution to the insight that makes it efficient.

---

## Repository Structure

```
engineering-excellence/
├── solutions/
│   ├── Arrays/
│   ├── BinaryTrees/
│   ├── Bit-Magic/
│   ├── Deque/
│   ├── Doubly-Linked-List/
│   ├── Linked-List/
│   ├── Mathematics/
│   ├── Matrix/
│   ├── POTD/
│   ├── Queue/
│   ├── Recursion/
│   ├── Sliding-Window/
│   ├── Stacks/
│   ├── Two-Pointers/
│   └── ...
└── utils/
    ├── setup_day.sh       # Dev environment setup
    ├── touch_new.sh       # Scaffold a new solution file
    └── sync_git.sh        # Git sync helper
```

---

## Live Sync with evolune.dev

This repository is connected to [evolune.dev](https://evolune.dev) via a webhook. Every push to `main` triggers a sync with the backend, updating the DSA progress page in real time.

Visit **[evolune.dev/dsa](https://evolune.dev/dsa)** to see:

- Total problems solved
- Topic-wise breakdown
- Difficulty distribution
- Recent activity

---

## Running a Solution

```bash
# Clone the repository
git clone https://github.com/kranthi/engineering-excellence.git
cd engineering-excellence

# Run any solution directly
python solutions/Arrays/subarray_with_given_sum.py
python solutions/BinaryTrees/top_view_bin_tree.py
python solutions/Recursion/get_permutations.py
```

No external dependencies — all solutions use Python standard library only.

---

## Philosophy

- **Two passes minimum** — brute force first, optimal second
- **Complexity always documented** — TC and AS for every approach
- **Patterns over problems** — notes capture the underlying technique, not just the answer
- **Runnable by default** — every file works as a standalone script

---

_Built and maintained by [Kranthi Kumar](https://evolune.dev) — updated with every problem solved._
