# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        p = root.left
        q = root.right

        def issame(p, q):
            if p and q:
                return p.val == q.val and issame(p.left, q.right) and issame(p.right, q.left)
            else:
                return p == q

        return issame(p, q)


if __name__ == '__main__':
    print([1, 2, 3] + [3])
