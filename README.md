# Leetcode-Problem-102

In this problem, the nodes of the Binary Tree has to be traversed level wise. After completing one level, every node of that level is appended into a list and at last this list is returned. 
For this problem, a queue has been used so that at each level, the nodes can be appended to it. Thus the time complexity of this approach is not more than O(n), as the maximum number of runs is equal to the number of nodes in the BT. The problem statement is as follows:

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000

Link to the problem: https://leetcode.com/problems/binary-tree-level-order-traversal/
