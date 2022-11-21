# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
# 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
import copy
class Solution:
    def letterCombinations(self, digits: str):
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        path = ''
        res = []

        def dfs(digits, start, path, res):
            if len(path) == len(digits):
                res.append(copy.deepcopy(path))
                return
            for start in range(start, len(digits)):
                for j in range(len(phone[digits[start]])):
                    # path.append(phone[digits[start]][j])
                    path += phone[digits[start]][j]
                    dfs(digits, start + 1, path, res)
                    path = path[: - 1]


        dfs(digits, 0, path, res)
        return res



if __name__ == '__main__':
    s = Solution()
    res = s.letterCombinations('23')
    print(res)