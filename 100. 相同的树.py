from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def pre_order_traverse(p, q):
            if not p and not q:
                return True

            if not p or not q or p.val != q.val:
                return False
            return pre_order_traverse(p.left, q.left) and pre_order_traverse(p.right, q.right)
        return pre_order_traverse(p, q)


if __name__ == '__main__':
    s = Solution()
    c = TreeNode(3)
    b = TreeNode(2)
    a = TreeNode(1, b, c)
    p = q = a
    res = s.isSameTree(p, q)
    print(res)