"""
Height Of Binary Tree (Easy)
@topic: BinaryTrees
@difficulty: easy
@tags: BinaryTree

Given a binary tree, the task is to find the height of the tree.
Height of the tree is the number of edges in the tree from the
root to the deepest node, Height of the empty tree is 0.

i/p:    1
      /   \
     2     3
    / \   / \
   4   5 6   7
o/p: 3

Approaches:
1. Recursive: Calculate height of left and right subtree for a node.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    """
    Recursively compute,
    Height of tree is maximum length of path from root to
    left subtree leaf node, room to right subtree leaf node.

    TC: O(n)
    AS: O(height), recursive call stack
    """

    # base case
    if root is None:
        return 0

    lh = height(root.left)
    rh = height(root.right)

    return 1 + max(lh, rh)


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
    print(height(root))  # 3
