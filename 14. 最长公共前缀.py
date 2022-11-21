from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = len(strs)
        n = 0
        start = 0
        if start == len(strs) - 1:
            return strs[0]


        def dfs(start, strs, n):
            if start >= len(strs) - 1:
               return True
            try:
                if strs[start][n] == strs[start + 1][n]:
                    return dfs(start + 1, strs, n)
            except Exception as e:
                return False
            else:
                return False
        while True:
            is_judge = dfs(start, strs, n)
            if not is_judge:
                return strs[0][:n]
            n += 1


if __name__ == '__main__':
    s = Solution()
    res = s.longestCommonPrefix(strs=["", ""])
    print(res)