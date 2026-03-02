# Binary Trees

## Introduction to Trees

Trees are non-linear data structure where information is stored in heirarchial structure, representing the levels and pointing nodes to its next level nodes.

Consider a linked list where nodes are linked with the pointer next to it, similarly tress are connected to its next nodes with linking more than one nodes.

### Basic Terminology:

- **Root** :- A root is the first node of the tree.
- **Edge** :- An edge is a link between any two nodes in the tree, and links only in forward direction, bi-directional linking between is not present.
- **Siblings**:- The children nodes of same parent are called siblings. Nodes with same parent are siblings.
- **Leaf of Node**:- A node is said to be leaf node, if no children nodes are present for the node.
- **Height of Tree**:- Height of tree is defined the length of path from root node to the node present at last level. Total number of levels in tree.

## Binary Tree

A nodes in tree consists of only two childern nodes is said to be binary tree. We can also say that children of nodes in binary tree can be 0, 1, or 2.

### Properties of Binary Tree:

- **Maximum number of nodes at level 'i' of a binary tree**: 2<sup>i-1</sup> Level of root is 1
- **Maximum number of nodes in binary tree of height h**: 2<sup>h-1<sup>.
- **Binary tree with N nodes, minimum height or minimum number of levels present**: log(N+1)

  ```
     Total number of nodes 'N' at height 'h' = 2<sup>h+1</sup>,

     => N = 2<sup>h+1</sup> - 1
     => N + 1 = 2<sup>h+1</sup>

     Applying "log" on both sides

     => log(N+1) = (h+1)*log(2)
     => h + 1 = log(N+1)
  ```

### Types of Binary Tree:

Based on the structure and number of parents and children nodes, a binary tree can be commonly
classified into these types:

#### 1. Full Binary:

A binary tree is full, if every nodes has either 0 or 2 nodes.

[!image]

#### 2. Complete Binary tree:

A binary tree is complete, when all the levels are filled except the last level and the last level has all keys as left as possible.

[!image]

#### 3. Perfect Binary tree:

A binary tree is perfect, when all the internal nodes have two children and all the leaves nodes are at same level.

[!image]

## Binary Tree Implementation

Binary tree is created with Node containing pointers of left and right children nodes.

To create the nodes at a level use queue data structure to insert the nodes for any node that doesnot children nodes.

```python

```

## Binary Tree Traversal

In Linear data structures we can traverse only in one logical way, either from start, end, or in middle, but in non-linear data structures traversing can happen in different ways.

Generally trees can be traverse in different ways, can be divided in to two major groups, generally used traversals and level order traversals.

So First we discuss about commonly used traversals.

### Preorder Traversal:

A node is processed before processing any of nodes in its subtree.
**Algorithm steps:**
[Self, Left, Right]

- visit the root.
- traverse left subtree
- traverse right subtree

#### Implementation

```python

```

### Postorder Traversal:

A node is processed after processing left subtree, rightsubtree
**Algorithm steps:**
[Left, Right, Self]

- Traverse left subtree
- Traverse right subtree
- visit root.

### Inorder Traversal:

A node is preocessed after processing all nodes in left subtree and right subtree nodes are processed after processing node itself.

**Algorithm steps:**
[left, self, right]

- Traverse left subtree
- visit root
- Traverse right subtree

### Height of Binary Tree

Given a binary tree, the task is to find the height of the tree. Height of the tree is the number of edges in the tree from the root to the deepest node, Height of the empty tree is 0.

#### Algorithm

Recursive calculate the height of left subtree and right subtree of node and assign height to the node as maximum of heights of children + 1.

```
- Recursively calculate the height of subtree
- if the tree is empty, return 0
- Take the left subtree, root->left and find its height
- Take the right subtree, root->right and find its height
- height of tree = max(height of left subtree, height of right subtree) + 1

```

## Level Order Traversal

In level order traversal, the binary tree is traversed or nodes are visited starting from root node to last level sequentially.

#### Alogorithm

We need a data structure to get the nodes in level order.
Initially we take the node and find its left, right. Then we need to append the node so that its left and right are considered. Now these left and right we again have to visit them for thier lefts and rights.
Consider a queue data structure,

```
- Push the first element in the queue
- Now loop, thorugh the q until it becomes empty.
- on each time, append the current nodes left and right to the queue
- pop the current top element of the queue and store as result
- at the end result contians level order traversal of nodes.
```


