# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root) -> bool:
        self.res = True
        djuge = root.val


        def traverse(root, djuge):
            if not root or self.res:
                return
            if root.val != djuge:
                self.res = False
                return False
            traverse(root.left, djuge)
            traverse(root.right, djuge)

        traverse(root, djuge)
        return self.res
