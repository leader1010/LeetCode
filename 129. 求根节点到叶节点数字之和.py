from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# backtracking
# class Solution:
#     def sumNumbers(self, root: Optional[TreeNode]) -> int:
#         temp = []
#         res = []
#
#         def pre_oreder_traverse(root):
#             if not root:
#                 return
#             temp.append(root.val)
#             if root and not root.left and not root.right:
#                 x = 0
#                 for i in range(len(temp)):
#                     x += temp[i] * 10 ** (len(temp) - 1 - i)
#                 res.append(x)
#
#             pre_oreder_traverse(root.left)
#             pre_oreder_traverse(root.right)
#             temp.pop()
#
#         pre_oreder_traverse(root)
#         return res

# dfs
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, num):
            if not node:
                return 0
            if not node.left and not node.right:
                return num * 10 + node.val
            return dfs(node.left, num * 10 + node.val) + dfs(node.right, num * 10 + node.val)

        return dfs(root, 0)


if __name__ == '__main__':
    s = Solution()
    c = TreeNode(3)
    b = TreeNode(2)
    a = TreeNode(1, None, c)
    res = s.sumNumbers(a)
    print(res)
