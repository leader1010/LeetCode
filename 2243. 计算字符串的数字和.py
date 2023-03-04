class Solution:
    def digitSum(self, s: str, k: int):
        temp = 0
        res = []
        while True:
            if len(s) >= k:
                s1 = s[0:k]
                for i in range(k):
                    temp += int(s1[i])
                res.append(str(temp))
                s = s[k:]
                temp = 0
            else:
                for i in s:
                    temp += int(i)
                res.append(str(temp))
                s = ""
                temp = 0
                for i in res:
                    s += i
                res.clear()
                if len(s) <= k:
                    return s


if __name__ == '__main__':
    s = Solution()
    res = s.digitSum('1234', 3)
    print(res)
