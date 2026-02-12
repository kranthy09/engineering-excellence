"""
Design a data structure With Max and Min.

The number which we are going to insert can be either minimum of
all minimums or maximum of all maximums.

Apply the following operations:

1. insertMin(x): Insert the minimum element x into the data structure.
2. insertMax(x): Insert the maximum element x into the data structure.
3. getMin(): Return the minimum element from the data structure.
4. getMax(): Return the maximum element from the data structure.
4. extractMin(): Remove and return the minimum element from the data structure.
5. extractMax(): Remove and return the maximum element from the data structure.

Time complexity of all operations should be O(1).
"""
from collections import deque


class MinMaxDeque:

    def __init__(self):
        self.q = deque()
        self._size = 0

    def insertmin(self, x):
        """
        Inserts minimum value in DS
        """
        self.q.appendleft(x)

    def insertmax(self, x):
        """
        Inserts maximum value in DS
        """
        self.q.append(x)

    def getmin(self):
        """
        Returns minimum from the DS
        """
        if self.q:
            return self.q[0]
        return -1

    def getmax(self):
        """
        Returns maximum from the DS
        """
        if self.q:
            return self.q[-1]
        return -1

    def extractmin(self):
        """
        Delete and return the minimum from the DS
        """
        if self.q:
            return self.q.popleft()
        return -1

    def extractmax(self):
        """
        Delete and return the maximum from the DS
        """
        if self.q:
            return self.q.pop()
        return -1


if __name__ == "__main__":
    ds = MinMaxDeque()
    ds.insertmin(1)
    ds.insertmax(10)
    print(ds.getmin())  # 1
    print(ds.getmax())  # 10
    print(ds.extractmin())  # 1
    print(ds.extractmax())  # 10
    print(ds.getmin())  # -1
    print(ds.getmax())  # -1
