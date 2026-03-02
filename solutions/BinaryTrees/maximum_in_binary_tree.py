"""
Maximum In Binary Tree (Easy)
@topic: BinaryTrees
@difficulty: easy
@tags: binarytree

Given a Binary Tree, find the maximum(or minimum) element in it.


i/o:        1
          /  \
         2    3
        /    / \
       4    5   6
      /    / \
     7    8   9


o/p: 9


Approaches:
1. Postorder Traversal through binarytree and track maximum
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def _calculate(root):
    """
    Recursive method for finding maximum in Binary Tree
    """
    # base case
    if root is None:
        # assume 'None' nodes have INT_MIN value
        return float("-inf")

    # find the left max
    leftmax = _calculate(root.left)

    # find the right max
    rightmax = _calculate(root.right)

    # current node data
    res = root.data

    # return max values of left subtree, right subtree and node's data
    return max(leftmax, rightmax, res)


def max_in_bin_tree(root):
    """
    Returns maximum of the binary tree by calculating
    recursively the maximum from left subtree, right subtree
    and current node.

    TC: O(n), visits all nodes in the tree.
    AS: O(H), recursive call stack.
    """
    # base case
    if root is None:
        return float("-inf")
    return _calculate(root)


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
    print(max_in_bin_tree(root))
