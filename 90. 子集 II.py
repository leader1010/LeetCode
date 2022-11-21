from typing import *


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        temp = []

        def dfs(res, temp):
            for i in range(len(nums)):
                temp.append(i)
                dfs(res, temp)
                temp.pop(i)
