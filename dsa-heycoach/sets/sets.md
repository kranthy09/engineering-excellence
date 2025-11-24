## 📌 Problem 1: Minimum Absolute Difference

Given a 0-indexed integer array nums and an integer k, find the minimum absolute difference between any two elements in the array that are at least k indices apart. Return the minimum absolute difference found.

### Example

```text
Input:
5
5 3 2 10 15
1
Output: 1
```

## 📌 Problem 2: Next Least Greater Element On Its Right

Given an array nums of n integers, replace every element with the least greater element on its right side in the array. If there are no greater elements on the right side, replace it with -1.

### Example

```text
Input:
15
8 58 71 18 31 32 63 92 43 3 91 93 25 80 28

Output: 18 63 80 25 32 43 80 93 80 25 93 -1 28 -1 -1

```

## 📌 Problem 3: Union And Intersection

Given two arrays, find their intersection and union and print the result in the solution function. A union between two arrays is defined as all the elements that occur in any one of the arrays. For example, if a = [1, 2, 2, 3, 4] and b = [1, 1, 3, 5, 6, 6], the union of these arrays is U = [1, 2, 3, 4, 5, 6]. The intersection between two arrays is defined as all the elements that are present in both arrays. Considering the same example, the intersection of those arrays is I = [1, 3].

### Example

```text
Input:
15
8 58 71 18 31 32 63 92 43 3 91 93 25 80 28

Output: 18 63 80 25 32 43 80 93 80 25 93 -1 28 -1 -1

```

## 📌 Problem 4: Unique Permutations

Given a string 's', return all the unique permutations of string 's' arranged in a lexicographical manner.

### Example

```text
Input:
abe

Output:
abe
aeb
bae
bea
eab
eba

```

## 📌 Problem 4: Jet Fighter Captain

You are in a war. You are handling an F-51 Fighter Jet and have to communicate with your allies. You are waiting for a command to confirm whether to attack or not. There is one issue though, you are not sure if your communication channel has been hacked or not.

To make sure that the message has been received from a trusted source, they will send you an array and an integer 'k'. Suppose the array can be divided into k or more than k segments where all segments's missing smaller value is same and is equal to segments first non negative value that is missing. (for example, in arr = {1, 3, 4, 0, 5}, that value will be 2 since it is the minimum non-negative value that is not present in the array) is the same. In that case, you have to print "Attack" else print "Wait".

Write an algorithm to help the pilot determine what he should do.

### Example

```text
Input:
6 2
0 1 0 1 0 1
Output:
Attack

Inpit:
3 3
0 1 0
output:
Wait

```

