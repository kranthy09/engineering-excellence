## Problems

1. Special Palindrome
2. Palindrome Integer
3. Power of a,b
4. Count of digits
5. count all digits in n numbers.

Mathematical - Algorithms

## Key Problems

### 1. Power of Numbers

### Given a number n, find the value of n raised to the power of its own reverse.

### Key Idea:

- How to compute large powers eliminating more computations.
- Calculate greater powers of numbers in logarithmic time.
- Used in practical approaches differentiate from other solutions.

```python
class Solution:
    def reverseexponentiation(self, n):
        base = n
        exp = 0
        n1 = n
        while n1:
            exp = exp*10 + n1%10
            n1//=10
        result = 1
        while exp > 0:
            if exp % 2 != 0:
                result *= base
            base = (base * base)
            exp >>= 1
        return result

```

### 2. Binomial Coefficient

### Given two integer values n and r, the task is to find the value of Binomial Coefficient nCr

### Key Idea:

- Compute largers divisions with gcd
- Practically used as it eliminates computations by gcd.

```python
from math import gcd

class Solution:
    def nCr(self, n, r):
        # code here
        # n, r, n-r
        # if n < r return 0;
        if n < r:
            return 0

        # numerator: n-r+1, n-r+2, ..., n
        # denominator: 1, 2, 3, 4,... r
        r = min(r, n-r)
        nume = 1
        deno = 1
        for i in range(r):
            nume *= (n-i)
            deno *= (i+1)
            g = gcd(nume, deno)
            nume //= g
            deno //= g
        return nume//deno


```


#### 1. Power of Numbers

#### 2. Binomial Coefficient

#### 3. Multiply Two Strings

### Pattern:

- Mathematically compute powers and divisions by reducing computations with a common or basic factor while performing calculations.

## Key Learnings

- Use Powers in competetive programming in logrithmic time.
- Reduce large divisions with by early divisions with gcd of two numbers.


### Steps to Concrete Practice

- There are more than 2 methods to solve power of numbers problem, solve them all with explanation written.
- Combinations have flaws in direct multiplication, explain it with gcd solution one after the other and this problem has more than 4 methods to solve.
- Multiplication of two strings, needs to be done in O(n\*m), solve in the naive approach instead of self.convert method.
