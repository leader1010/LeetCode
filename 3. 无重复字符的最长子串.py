from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        if len(s) == 2:
            if s[0] == s[1]:
                return 1
            else:
                return 2
        slow, fast = 0, 0
        temp = 0
        d = defaultdict(lambda: 0)
        d[s[slow]] += 1
        # d[s[fast]] += 1
        while True:
            if fast == len(s) - 1:
                if d[s[slow]] <= 1 and d[s[fast]] <= 1:
                    temp = (fast - slow + 1) if (fast - slow + 1) > temp else temp
                    return temp
                else:
                    temp = (fast - slow) if (fast - slow) > temp else temp
                    return temp
                # temp = (fast - slow + 1) if (fast - slow + 1) > temp else temp
            if d[s[slow]] <= 1 and d[s[fast]] <= 1:
                temp = (fast - slow + 1) if (fast - slow + 1) > temp else temp
                fast += 1
                d[s[fast]] += 1
            else:
                temp = (fast - slow) if (fast - slow) > temp else temp
                d[s[slow]] -= 1
                slow += 1


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("abab")
    print(res)


