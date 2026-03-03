"""
Level Order Traversal (Medium)
@topic: BinaryTrees
@difficulty: medium
@tags: binarytree, queue

Given a tree, returns its level order traversal of nodes.

i/o:        1
          /   \
         2     3
        / \
       4   5

o/p: [1, 2, 3, 4, 5]


Approaches:
1. Expected: use a queue to store the next levels children.
"""
from collections import deque


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def level_order_traversal(self, root):
        """
        Consider a queue and append its children to queue before
        pop top element out of queue.
        Store the removed element in the result, having
        level order traversal of binary tree

        TC: O(n)
        AS: O(n)
        """

        # base case
        if root is None:
            return []

        # output array
        res = []

        q = deque()

        # append root to the queue
        q.append(root)

        while q:
            # take the top element from queue,
            # each node at current level
            node = q.popleft()

            # append to current level node to output
            res.append(node.data)

            # if there is left node append its children
            if node.left:
                q.append(node.left)

            # if there is right node append its children
            if node.right:
                q.append(node.right)
        return res


if __name__ == "__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(8)
    """
    Input Tree:
            1
          /   \
         2     3
        / \     \
       4   5     8
    """
    ans = Solution()
    print(ans.level_order_traversal(root))  # [1, 2, 3, 4, 5, 8]
