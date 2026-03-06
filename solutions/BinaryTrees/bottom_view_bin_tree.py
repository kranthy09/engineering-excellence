"""
Bottom View Bin Tree (Easy)
@topic: BinaryTrees
@difficulty: easy
@tags: binarytree

Given a Binary Tree. The task is to print the nodes of the binary tree
when viewed from bottom. That is, the bottom view of the binary tree will
contain only those nodes that can be seen when the Binary tree is
viewed from the bottom in 3-dimensional.

i/o:       1
          /  \
         2    3
        /    / \
       4    5   6
      /    / \
     7    8   9

o/p: [7, 8, 9, 6]


Approaches:
1. Expected: nodes at bottom have same distances.
"""


from typing import List
from collections import deque


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bottom_view(root: Node) -> List[int]:
    """

    TC:
    AS:
    """
    pass


def bottom_view_iter(root):
    """
    Store the level of nodes in queue with their
    horizantal distance (HD) as key and data as value

    TC:
    AS:
    """
    # since we are dealing with nodes
    # their might be None nodes
    # base case

    # queue to store nodes at each level
    q = deque()

    # push root node, with depth as 0
    q.append((root, 0))

    # height distance node hashmap
    hmap = {}

    while q:
        node, hd = q.popleft()
        if hmap.get(hd):
            hmap[]


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.right = Node(7)
    # Tree structure:
    #       1
    #      / \
    #     2   3
    #    /   / \
    #   4   5   6
    #        \
    #         7
    print(bottom_view(root))
    #
    print(bottom_view_iter(root))
    # [4, 2, 1, 3, 6]
