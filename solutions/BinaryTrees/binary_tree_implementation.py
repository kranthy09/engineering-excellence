"""
Binary Tree From Arr (Easy)
@topic: BinaryTree
@difficulty: easy
@tags: implementation, binarytree


Create a binary tree from list of numbers

i/o: [1, 2, 3, 4, 5, 6, 7]
o/p:    1
      /   \
     2     3
    / \   / \
   4   5 6   7


Approaches:
1. use an intermediary queue to replicate tree node behaviour.
"""

from collections import deque


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert(self, val):
        """
        Insert a node in the binary tree, left node inserted first.

        TC: O(height)
        AS: O(1)
        """
        # base case
        if self.root is None:
            self.root = Node(val)
            print("inserted {}".format(val))
            return

        q = deque()
        q.append(self.root)

        while q:  # noqa
            node = q.popleft()
            new_node = Node(val)
            if node.left is None:
                node.left = new_node
                print("inserted {}".format(val))
                return
            q.append(node.left)
            if node.right is None:
                node.right = new_node
                print("inserted {}".format(val))
                return
            q.append(node.right)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]

    bintree = BinaryTree()
    for ele in arr:
        bintree.insert(ele)
