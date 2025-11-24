## Data Structure - Array

Continous memory allocation of data, with O(1) space complexity to access any element with an index.

- Collection of data with somedata type
- Collection is sorted in contigous memory space.

### Access an element

In an array, to access an element, at an index 'i', is arr[i].

- when an array is defined, 'arr', address of the first element is store in the variable 'arr', which is generally known as base address
- On accessing the value at ith index, address is calculated by,
- - address of the ith index = Base Address + i \* dataSize
- After calculating the address of ith index, arr[i] dereferences the value at i.

## Dynamic Array

When an array size cannot be predicted, dynamic arrays are defined that internally has an abstraction which implements the functionality to increase the size of the array.

## Memory Fragementation

In an multiprocessor system, there can be different programs running, and in that situation if there is a need to create an array of some datatype elements. The space required to create the array should be in contigous nature, but due to other programs the processor can be able to provide contigous memory blocks to create the array. In that case LinkedLists can be help full to store the elements.

```quote
LinkedLists next topic
```

# 📝 Count of Anagram Occurrences in a String – Sliding Window + HashMap

## 🚀 Problem Statement

Given two strings `text` and `pattern`, return the number of substrings of `text` that are anagrams of `pattern`.

### 🧩 Example:

Input: text = "cbaebabacd", pattern = "abc"
Output: 2
Explanation: The anagrams are "cba" and "bac"

---

## 🧠 Understanding the Problem

We're looking for substrings in `text` that are:

- Same length as `pattern`, and
- Contain the same characters with the same frequency, in any order.

In the example, `"cba"` and `"bac"` are both anagrams of `"abc"`.

---

## 🐢 Naive Approach

Check every substring of `text` with the length of `pattern`:

1. Generate all substrings.
2. For each, check if it's an anagram of `pattern`.

### 🔁 Time Complexity:

- Generating substrings: `O(n)`
- Comparing with pattern: `O(k log k)` (if sorted) or `O(k)` with frequency count

🕒 Total: `O(n × k)`, where `n` is the length of `text`, and `k` is the length of `pattern`.

---

## ⚡ Optimized Approach – Sliding Window + Hash Map

We'll use the **sliding window** technique with a **frequency map** to reduce time complexity to `O(n)`.

### 🔧 Core Idea:

- Keep a frequency count of characters in `pattern`.
- Move a window of length `len(pattern)` across `text`.
- Maintain a frequency count of the current window and compare it with the `pattern` count.

---

## 🧑‍💻 Python Code

````python
from collections import Counter

def count_anagrams(text, pattern):
    k = len(pattern)
    n = len(text)
    if k > n:
        return 0

    pattern_count = Counter(pattern)
    window_count = Counter(text[:k])
    count = 0

    if window_count == pattern_count:
        count += 1

    for i in range(k, n):
        # Remove char going out of the window
        window_count[text[i - k]] -= 1
        if window_count[text[i - k]] == 0:
            del window_count[text[i - k]]

        # Add new char to the window
        window_count[text[i]] += 1

        # Compare frequency maps
        if window_count == pattern_count:
            count += 1

    return count
```

