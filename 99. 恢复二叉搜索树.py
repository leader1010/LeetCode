from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.first_node = None
        self.second_node = None
        self.pre_node = TreeNode(float('-inf'))

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traversal(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val

    def traversal(self, node):
        if not node:
            return
        self.traversal(node.left)
        if not self.first_node and self.pre_node.val >= node.val:
            self.first_node = self.pre_node
        if self.first_node and self.pre_node.val >= node.val:
            self.second_node = node
        self.pre_node = node
        self.traversal(node.right)
