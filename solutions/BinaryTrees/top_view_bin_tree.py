"""
Top View Bin Tree (Easy)
@topic: BinaryTrees
@difficulty: easy
@tags: binarytree


Given a Binary Tree. The task is to print the nodes of the binary tree
when viewed from top. That is, the top view of the binary tree will
contain only those nodes that can be seen when the Binary tree is
viewed from the top in 3-dimensional.

i/o:       1
          /  \
         2    3
        /    / \
       4    5   6
      /    / \
     7    8   9

o/p: [1, 3, 6, 9]


Approaches:
1. Expected: Recursive approach
"""


from typing import List
from collections import deque


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def top_view(root: Node) -> List[int]:
    """

    TC:
    AS:
    """
    pass


def top_view_iter(root):
    """
    Store the level of nodes in queue with their
    horizantal distance (HD) as key and data as value

    TC:
    AS:
    """
    # base case
    if root is None:
        return 0

    q = deque()
    hmap = {}

    # push root and its hd = 0
    q.append((root, 0))

    while q:

        node, hd = q.popleft()

        if hd not in hmap:
            hmap[hd] = node.data
        if node.left:
            # send its left along with hd
            # left subtree node is hd - 1 from root node
            q.append((node.left, hd - 1))
        if node.right:
            # send its right along with hd
            # right subtree node is hd + 1 from root node
            q.append((node.right, hd + 1))

    # resultant output
    res = []
    for key in sorted(hmap.keys()):
        res.append(hmap[key])

    return res


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
    print(top_view(root))
    #
    print(top_view_iter(root))
    # [4, 2, 1, 3, 6]
