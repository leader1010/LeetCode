import copy


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumRootToLeaf(self, root) -> int:
        temp = []
        res = 0

        def traverse(root, res):
            if not root:
                a = ''.join(temp)
                res += int(a, 2)
                temp.pop(-1)
                return
            temp.append(root.val)
            traverse(root.left, res)
            traverse(root.right, res)

        traverse(root, res)
        return res
