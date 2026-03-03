"""
Left View Bin Tree (Easy)
@topic: BinaryTrees
@difficulty: easy
@tags: binarytree

Given a Binary Tree. The task is to print the nodes of the binary tree
when viewed from left side. That is, the left view of the binary tree will
contain only those nodes that can be seen when the Binary tree is
viewed from the left.

i/o:       1
          /  \
         2    3
        /    / \
       4    5   6
      /    / \
     7    8   9

o/p: [1, 2, 4, 7]

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


def left_view(root):
    """
    Recursive method to get values from a binary
    tree, viewed from left side.

    TC: O(n), visits all nodes once.
    AS: O(H), recursive call stack
    """

    res = []
    max_level_reached = [-1]

    def left_view_util(root, max_level_reached, current_level):
        # base case
        if root is None:
            return

        if current_level > max_level_reached[0]:
            res.append(root.data)
            max_level_reached[0] = current_level
        left_view_util(root.left, max_level_reached, current_level + 1)
        left_view_util(root.right, max_level_reached, current_level + 1)

    left_view_util(root, max_level_reached, 0)

    return res


def left_view_iter(root):
    """
    Iterative method to get values of binary tree
    when viewed from left side

    Consider queue datastrucutre and do level order
    traversal to capture the results of each levels
    first(top) elements in the queue

    TC:
    AS:
    """
    res: List = []
    # base case

    # always maintains first left node at
    # each level
    q = deque()

    # push the root node
    q.append(root)

    # push a delimiter to identify each level
    q.append(None)

    while q:

        # take the top
        node: Node = q.popleft()
        # if the top is node
        if node:
            # capture the data, as it is left node
            res.append(node.data)

            # empty the remaining level elements with
            # help of 'None' delimitter
            while node is not None:

                # push the left subtree of the node for next
                # level order traversal
                if node.left:
                    q.append(node.left)
                # push the right subtree of the node for next
                # level order traversal
                if node.right:
                    q.append(node.right)
                # remove the current top node and update it to next
                # incoming node.
                node = q.popleft()
            # add delimitter for the each level
            q.append(None)
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
    print(left_view(root))
    # [1, 2, 4, 7]
    print(left_view_iter(root))
