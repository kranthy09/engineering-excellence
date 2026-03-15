"""
Vertical Tree Traversal (Medium)
@topic: potd
@difficulty: medium
@tags: binarytree

Given the root of a Binary Tree, find the vertical
traversal of the tree starting from the leftmost
level to the rightmost level.

Note: If there are multiple nodes passing through a
vertical line, then they should be printed as they
appear in level order traversal of the tree.

i/o: root = [1, 2, 3, 4, 5, 6, 7, N, N, N, 8, N, 9, N, 10, 11, N]
o/p: [[4], [2], [1, 5, 6, 11], [3, 8, 9], [7], [10]]


Approaches:
1. Brute Force:
2. Expected:
"""

from collections import deque, defaultdict


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def vertical_order(self, root):
        """

        TC: O(n)
        AS: O(n)
        """

        # base case
        if root is None:
            return []

        q = deque()
        res = []

        deps = defaultdict(list)
        mx = float("-inf")
        mn = float("inf")

        q.append([root, 0])
        while q:
            node, level = q.popleft()
            mx = max(mx, level)
            mn = min(mn, level)
            deps[level].append(node.data)

            if node.left:
                q.append([node.left, level-1])
            if node.right:
                q.append([node.right, level+1])

        for val in range(mn, mx+1):
            res.append(deps[val])

        return res


if __name__ == "__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(8)

    result = Solution().vertical_order(root)
    print(result)

    # [[4], [2], [1, 5, 8], [3]]
