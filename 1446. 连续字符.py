class Solution:
    def maxPower(self, s: str) -> int:
        x = s[0]
        count = 0
        res = 0
        for i in s:
            if x == i:
                count += 1
                res = res if res > count else count
            else:
                res = res if res > count else count
                count = 1
                x = i
        return res


if __name__ == '__main__':
    s = Solution()
    res = s.maxPower("leetcode")
    print(res)