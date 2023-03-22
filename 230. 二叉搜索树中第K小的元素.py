from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def in_order_traverse(root):
            if not root:
                return
            in_order_traverse(root.left)
            res.append(root.val)
            in_order_traverse(root.right)

        in_order_traverse(root)
        return res[k - 1]
