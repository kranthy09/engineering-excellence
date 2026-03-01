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
