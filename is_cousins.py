"""
In a binary tree, the root node is at depth 0,
and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have
the same depth, but have different parents.

We are given the root of a binary tree with unique
values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to
the values x and y are cousins.
"""

def get_level_and_parent(root, val, parent, lev):
    if root is None:
        return (0,parent)
    if root.val == val:
        return (lev, parent)
    obj = get_level_and_parent(root.left, val, root, lev+1)
    if obj[0] > 0:
        return obj
    return get_level_and_parent(root.right, val, root, lev+1)


def is_cousins(root, x, y):
    level_of_x, parent_of_x = get_level_and_parent(root,x, None,1)
    level_of_y, parent_of_y = get_level_and_parent(root,y, None,1)
    if level_of_x == level_of_y and parent_of_x != parent_of_y:
        return True
    return False