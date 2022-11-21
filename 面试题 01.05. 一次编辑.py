class Solution(object):
    def oneEditAway(self, first, second):
        M, N = len(first), len(second)
        if abs(M - N) > 1:
            return False
        if N == M + 1:
            return self.oneEditAway(second, first)
        i, j = 0, 0
        diff = 0
        while i < M and j < N:
            if first[i] != second[j]:
                diff += 1
                if diff >= 2:
                    return False
                if M > N:
                    j -= 1 # 为了让原地等待，先回退一步，后面会再向右移动一步
            i += 1 # 每次都向右移动一步
            j += 1 # 每次都向右移动一步
        return True


