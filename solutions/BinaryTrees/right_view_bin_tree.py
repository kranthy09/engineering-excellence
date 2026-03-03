"""
Right View Bin Tree (Easy)
@topic: BinaryTrees
@difficulty: easy
@tags: binarytree

Given a Binary Tree. The task is to print the nodes of the binary tree
when viewed from right side. That is, the right view of the binary tree will
contain only those nodes that can be seen when the Binary tree is
viewed from the right.

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


def right_view(root: Node) -> List[int]:
    """
    Recursive method to get values from a binary
    tree, viewed from right side.

    TC: O(n), visits all nodes once.
    AS: O(H), recursive call stack
    """
    res: List = []

    max_level_reached: List = [-1]

    def right_view_util(
        root: Node, max_level_reached: List, current_level: int
    ):

        # base case
        if root is None:
            return

        # current level reached is compared with max level
        # so that it doesn't block the right view
        if current_level > max_level_reached[0]:
            res.append(root.data)
            max_level_reached[0] = current_level

        # ask recursion to give right view of right subtree
        right_view_util(root.right, max_level_reached, current_level + 1)
        # ask recursion to give right view of left subtree
        right_view_util(root.left, max_level_reached, current_level + 1)

    # init recursion, at root level is 0.
    right_view_util(root, max_level_reached, 0)

    return res


def right_view_iter(root):
    """
    Iterative method to get values of binary tree
    when viewed from right side

    Consider queue datastrucutre and do level order
    traversal to capture the results of each levels
    first(top) elements in the queue

    TC:
    AS:
    """
    res = []

    # base case

    q = deque()

    # push the root of the tree
    q.append(root)

    # push the delimitter as 'None" for each level
    q.append(None)

    while q:

        # top element will be current level right element

        # take the top element
        node: Node = q.popleft()
        # if it is not delimitter
        if node:
            # append it to result, current level right element.
            res.append(node.data)

            # remove the remaining row level nodes with
            # 'None' delimitter in queue for each row
            while node is not None:

                # if the node has children append in right first
                if node.right:
                    q.append(node.right)

                # left later so that queue can maintian right view elements
                # at the top of it.
                if node.right:
                    q.append(node.left)
                # remove the top elements to till obtaining delimitter
                # update node after each node remove
                node = q.popleft()
            # add delimitter for each row after processing its nodes
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
    print(right_view(root))
    # [1, 3, 6, 7]

    print(right_view_iter(root))
    # [1, 3, 6, 7]
