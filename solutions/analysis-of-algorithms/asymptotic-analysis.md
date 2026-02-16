#### Asymptotic Analysis:

You can’t reach a goal faster than its Ω (best-case) or afford to drift beyond its O (worst-case).

Compute your Θ (tight bound), then engineer your actions to push relentlessly toward the lower bound to reache goal in optimal time.

#AsymptoticAnalysis #BigO #AlgorithmicThinking #Optimization

# Asymptotic Analysis Practice: Attention to Detail

## Question 1: String Output in Nested Loops

**Category:** Hidden Operations in Code

```cpp
for(i=0; i<n; i++){
    for(j=i+1; j<n; j++){
        cout << <string> << endl;
    }
}
```

**Your Task:** Find the **tight bound** time complexity.

**Answer:**

---

## Question 2: Sorting Strings Array

**Category:** Applying Given Time Complexities

**Given:**

- Sorting a string: O(n log n)
- Comparing two strings: O(m)

**Problem:**

```
strings = ["abs", "cdg", "aet", "sgr"]
```

Sort each string in the array, then sort the strings array in lexicographical order.

**Your Task:** Find the overall time complexity.

**Answer:**

---

## Question 3: Matrix Initialization Pattern

**Category:** Hidden Operations in Code

```cpp
int matrix[n][n];
for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
        matrix[i][j] = i * j;
    }
}
```

**Your Task:** Find the time and space complexity. Pay attention to ALL operations.

**Answer:**

---

## Question 4: String Concatenation in Loop

**Category:** Hidden Operations in Code

```cpp
string result = "";
for(int i = 0; i < n; i++){
    result += "a";
}
```

**Your Task:** Find the time complexity. (Hint: String concatenation is NOT O(1))

**Answer:**

---

## Question 5: Binary Search with String Comparison

**Category:** Applying Given Time Complexities

**Given:**

- Binary search iterations: O(log n)
- String comparison: O(m) where m is the length of strings

**Problem:**

```
arr = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
```

Search for "cherry" using binary search in this sorted array of strings.

**Your Task:** Find the time complexity of this search operation.

**Answer:**

---

## Question 6: Nested Loop with Break Condition

**Category:** Hidden Operations in Code

```cpp
for(int i = 0; i < n; i++){
    for(int j = 0; j < n; j++){
        if(j == i) break;
        cout << "*";
    }
}
```

**Your Task:** Find the TIGHT BOUND time complexity. How many stars are printed?

**Answer:**

---

## Question 7: HashMap Operations

**Category:** Applying Given Time Complexities

**Given:**

- HashMap insertion: O(1) average case
- HashMap lookup: O(1) average case
- String hashing: O(k) where k is string length

**Problem:**

```cpp
unordered_map<string, int> map;
for(int i = 0; i < n; i++){
    map[words[i]]++;  // words[i] has average length m
}
```

**Your Task:** Find the time complexity considering the hashing operation.

**Answer:**

---

## Question 8: Recursive Function Analysis

**Category:** Hidden Operations in Code

```cpp
void print(int n){
    if(n <= 0) return;
    for(int i = 0; i < n; i++){
        cout << "*";
    }
    print(n - 1);
}
```

**Your Task:** Find the time complexity when calling `print(n)`. How many stars are printed total?

**Answer:**

---

## Question 9: Sorting with Custom Comparator

**Category:** Applying Given Time Complexities

**Given:**

- Merge sort comparisons: O(n log n)
- Custom comparator for objects: O(k) where k is number of fields compared

**Problem:**

```cpp
struct Person {
    string firstName;  // avg length: f
    string lastName;   // avg length: l
    int age;
};

// Sort n persons by lastName, then firstName, then age
sort(persons.begin(), persons.end(), customComparator);
```

**Your Task:** Find the time complexity of sorting, considering string comparisons in the comparator.

**Answer:**

---

## Question 10: Two Pointer with String Operations

**Category:** Hidden Operations in Code

```cpp
string text = "...";  // length n
int left = 0, right = n - 1;
while(left < right){
    if(text.substr(left, right - left + 1) == palindrome){
        count++;
    }
    left++;
    right--;
}
```

**Your Task:** Find the time complexity. (Hint: What does `substr()` do?)

**Answer:**

---

## Question 11: Building Result Array

**Category:** Hidden Operations in Code

```cpp
vector<int> result;
for(int i = 0; i < n; i++){
    result.push_back(i);
}
```

**Your Task:** Find the amortized time complexity vs worst-case time complexity for this code.

**Answer:**

---

## Question 12: Graph BFS with String Nodes

**Category:** Applying Given Time Complexities

**Given:**

- BFS visits each node once: O(V + E)
- String comparison for visited check: O(m)
- Using unordered_set<string> for visited tracking

**Problem:**

```
Graph has V vertices (string labels of avg length m) and E edges
```

**Your Task:** Find the time complexity of BFS considering string operations.

**Answer:**

**Short Notes:**

Worst, Average, Best Case:

- Upper, lower and tight bounds.

Asymptotic Notations:

- Theta(exact), Omega(atleast), Big O(atmost)

Upper Bound: Intha kanna slow ga run avvadu, input size entha unna
Lower Bound: Intha kanna fast runtime algo ledu
Tight Bound: Average of all types of input sizes and data types distribution for all cases.

Tight Bound is between Lower and Upper bound.

Upper bound is used to compare algorithms growth over input sizes.
