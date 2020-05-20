"""
Given a binary search tree, write a function kthSmallest
to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    def inorder(root):
        if root is None:
            return []
        return [*inorder(root.left), root.val, *inorder(root.right)]

    return inorder(root)[k-1]
