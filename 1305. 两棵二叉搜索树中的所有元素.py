# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1, root2):

        temp = []
        def pre_order_traverse(root, temp):
            if not root:
                return
            pre_order_traverse(root.left, temp)
            temp.append(root.val)
            pre_order_traverse(root.right, temp)

