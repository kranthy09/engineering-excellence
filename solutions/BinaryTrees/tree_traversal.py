"""
Tree Traversal (Easy)
@topic: BinaryTrees
@difficulty: easy
@tags: BinaryTree

Preorder Traversal
Postorder Traversal
Inorder Traversal

"""


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    """
    Recursive approach for preorder traversal on binary tree

    Order: Self, Left, Right

    TC: O(n)
    AS: O(H), recursive call stack from root to leaf.
    """

    # base case
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    """
    Recursive approach for postorder traversal of
    binary tree

    order: left, right, self

    TC: O(n)
    AS: O(H), recursive call stack
    """
    # base case
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


def inorder(root):
    """
    Recursive approach for inorder traversal of
    binary tree

    order: left, self, right

    TC: O(n)
    AS: O(H), recursive call stack
    """

    # base case
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(20)
    root.left.left = Node(40)
    root.left.right = Node(50)
    root.left.right.left = Node(70)
    root.left.right.right = Node(80)
    root.right = Node(30)
    root.right.right = Node(60)

    preorder(root)  # 1 20 40 50 70 80 30 60
    print()
    postorder(root)  # 40 70 80 50 20 60 30 1
    print()
    inorder(root)
    print()  # 40 20 70 50 80 1 30 60
