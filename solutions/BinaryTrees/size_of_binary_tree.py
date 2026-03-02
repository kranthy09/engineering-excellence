"""
Size Of Binary Tree (Easy)
@topic: BinaryTrees
@difficulty: easy
@tags: binarytree

Given a binary tree finds its size., number of nodes present in the
binary tree.

i/o:        1
          /   \
         2     3
        / \
       4   5

o/p: 5


Approaches:
1. Recursive: For a node, add size of left and right subtree + 1(current node)
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def size(root):
    """
    Recursively finds the size of a Binary Tree

    TC:
    AS:
    """
    # base case
    if root is None:
        return 0

    # find the size of left subtree
    left_size = size(root.left)

    # find the size of right subtree
    right_size = size(root.right)

    # add the size of left, right and current node(1).
    return 1 + left_size + right_size


if __name__ == "__main__":
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    """
    Input Tree:
            1
          /   \
         2     3
        / \
       4   5
    """
    print(size(root))  # 5
