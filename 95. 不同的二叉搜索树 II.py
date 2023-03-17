# Definition for a binary tree node.\
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0: # 如果节点数量为 0，则返回一个空列表
            return []
        return self.build(1, n) # 构造闭区间 [1, n] 的 BST

    def build(self, lo: int, hi: int) -> List[TreeNode]:
        res = []
        # 当 lo > hi 时，不存在节点，将 None 存入结果列表中，并返回
        if lo > hi:
            res.append(None)
            return res

        # 1、穷举 root 节点的所有可能。
        for i in range(lo, hi + 1):
            # 2、递归构造出左右子树的所有合法 BST。
            leftTree = self.build(lo, i - 1)
            rightTree = self.build(i + 1, hi)
            # 3、给 root 节点穷举所有左右子树的组合。
            for left in leftTree:
                for right in rightTree:
                    # i 作为根节点 root 的值
                    root = TreeNode(i)
                    root.left = left
                    root.right = right
                    res.append(root)

        return res



