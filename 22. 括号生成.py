from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        visited = [False for _ in range(2*n)]
        strs = "(" * n + ")" * n
        temp = ""
        res = []
        def dfs(temp, res, visited):
            if temp.count("(") < temp.count(")"):
                return
            if len(temp) == 2*n:
                res.append(temp)
                return

            for i in range(2*n):
                print(f"i{i}")
                if i > 0 and strs[i] == strs[i - 1] and not visited[i - 1]:
                    continue
                if not visited[i]:

                    temp += strs[i]
                    visited[i] = True
                    dfs(temp, res, visited)
                    temp = temp[:-1]
                    visited[i] = False

        dfs(temp, res, visited)
        print(len(res))
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.generateParenthesis(2)
    print(res)


