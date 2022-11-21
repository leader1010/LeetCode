class Solution:
    def maxPoints(self, points) -> int:
        row = len(points)
        col = len(points[0])
        dp = [[0] * col for _ in range(row)]

        for i in range(1, row):
            n_dp = [0] * col
            lmax = 0
            for j in range(col):
                lmax = max(lmax-1, dp[j])






