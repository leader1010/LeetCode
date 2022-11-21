class Solution:
    def makesquare(self, matchsticks: list) -> bool:
        length = sum(matchsticks) // 4
        matchsticks.sort()
        temp = 0
        path = []
        res = []

        def dfs(length, sticks, path, res, j):
            if j == len(sticks):
                return
            path += sticks[j]

            if path > length:
                return
            elif path == length:
                res.append()
            dfs(length, sticks, path, res, j+1)



        for i in range(len(matchsticks)):
            dfs(length, matchsticks, path, res, i)



if __name__ == '__main__':

    s = Solution()
    s.makesquare()
