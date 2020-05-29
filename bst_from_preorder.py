"""
Return the root node of a binary search tree that
matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where
for every node, any descendant of node.left has a value < node.val,
and any descendant of node.right has a value > node.val.  Also recall
that a preorder traversal displays the value of the node first, then
traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible
to find a binary search tree with the given requirements.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def bsf_from_preorder(pre):
    stack = []
    root = TreeNode(pre[0])

    stack.append(root)
    i = 1
    size = len(pre)

    while i < size:
        temp = None

        while (len(stack) > 0 and pre[i] > stack[-1].val):
            temp = stack.pop()

        if temp is None:
            temp = stack[-1]
            temp.left = TreeNode(pre[i])
            stack.append(temp.left)
        else:
            temp.right = TreeNode(pre[i])
            stack.append(temp.right)
        i += 1
    return root