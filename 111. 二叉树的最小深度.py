from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def minDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         res = []
#         minDepth = 0
#
#         def pre_order_traverse(root, minDepth, desc=True):
#             if root and not root.left and not root.right:
#                 res.append(minDepth)
#             if not root:
#                 return
#             minDepth += 1
#             pre_order_traverse(root.left, minDepth)
#             pre_order_traverse(root.right, minDepth)
#
#         pre_order_traverse(root, minDepth)
#         return min(res)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if not root.right:
            return self.minDepth(root.left) + 1
        if not root.left:
            return self.minDepth(root.right) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


if __name__ == '__main__':
    s = Solution()
    c = TreeNode(3)
    b = TreeNode(2)
    a = TreeNode(1, b)
    res = s.minDepth(a)
    print(res)
