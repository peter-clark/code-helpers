# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepth(self, root):
    """
    : gets max depth of a tree
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    l_d = self.maxDepth(root.left) # recurse
    r_d = self.maxDepth(root.right) # recurse

    return max(l_d, r_d)+1 # here is where the +1 is added for each level