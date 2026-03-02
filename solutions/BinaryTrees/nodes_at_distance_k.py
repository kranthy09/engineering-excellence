"""
Nodes At Distance K (Easy)
@topic: BinaryTrees
@difficulty: easy
@tags: binarytree

Given a root of a tree, and an integer k. Print all the nodes
which are at k distance from root.


i/o: k = 2
            1
          /   \
        2      3
      /  \    /
    4     5  8

o/p: 4, 5, 8


Approaches:
1. Recursive: calculate the height of each node in left and right.
"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def _calculate(root, depth, k, res):
    """
    Recursive function to calculate nodes of
    path length equal to k
    we should send the node with it current depth.
    """
    # base case
    if root is None:
        return

    # we get node and its depth,
    # if it is k,
    if depth == k:
        res.append(root.data)
        return

    _calculate(root.left, depth + 1, k, res)
    _calculate(root.right, depth + 1, k, res)


def nodes_at_k_dis(root, k):
    """
    Divide the tree in to leftsub tree and
    right subtree, send leftsubtree with its current node's
    depth, and send left subtree with its current node's
    depth, when the depth hits k, then capture the node's data
    nodes at distance less than k are early returned.

    TC: O(n), visits every node once
    AS: O(k), recursive call stack
    """
    # result variable
    res = []

    # root node is at depth 0.
    _calculate(root, 0, k, res)

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
        / \
       4   5
    """
    print(nodes_at_k_dis(root, 2))  # [4, 5, 8]
