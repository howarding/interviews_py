# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3
# But the following [1,2,2,null,3,null,3] is not:
#       1
#      / \
#     2   2
#      \   \
#      3    3
# Note:
# Bonus points if you could solve it both recursively and iteratively.

from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution_101(object):
    # Recursive
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return not root or self.helper(root.left, root.right)

    def helper(self, left, right):
        """
        :type left: TreeNode
        :type right: TreeNode
        :rtype: bool
        """
        if not left and not right:
            return True
        if (not left) != (not right):
            return False
        return left.val == right.val \
               and self.helper(left.left, right.right) \
               and self.helper(left.right, right.left)


    # Iterative
    def isSymmetric1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lefts = deque([root.left])
        rights = deque([root.right])
        while lefts and rights:
            left = lefts.popleft()
            right = rights.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            lefts.extend([left.left, left.right])
            rights.extend([right.right, right.left])
        return True


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(3)
sol = Solution_101()
print sol.isSymmetric1(root)
