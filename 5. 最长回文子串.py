class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = {}
        for i in range(1, len(s)):
            left = i - 1
            right = i + 1

            while True:
                if left < 0 or right > len(s) - 1:
                    temp = right - left -2
                    res[temp] = [left + 1, right - 1]
                    break
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    temp = right - left -2
                    res[temp] = [left + 1, right - 1]
                    break
        key_s = max(res.keys())
        return s[res[key_s][0]: res[key_s][-1] +1]

if __name__ == '__main__':
    s = Solution()
    res = s.longestPalindrome("babad")
    print(res)



