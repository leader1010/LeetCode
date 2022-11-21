class Solution:
    def reverseWords(self, s: str) -> str:
        y = s.strip().split()
        res = ""
        for i in range(len(y) - 1, -1,-1):
            res += f"{y[i]} "
        return res.strip()


if __name__ == '__main__':
    s = Solution()
    res = s.reverseWords("a good   example")
    print(res)




