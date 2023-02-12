from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        lst = [i for i in range(10)]
        visted = [False for _ in range(10)]
        res = []
        temp = []

        def dfs(visited, k, n):

            for i in range(10):
                if not visited[i]:
                    temp.append(i)
                    visited[i] = True
                    dfs(visited, k, n)
                    visited[i] = True




