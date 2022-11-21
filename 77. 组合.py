import copy
class Solution:
    def combine(self, nums: list, n):
        nums = [i for i in range(1, n + 1)]
        temp = []
        res = []


        def dfs(start, nums, temp, res, n):
            if n == len(temp):
                res.append(copy.deepcopy(temp))
                return

            for start in range(start, len(nums)):
                    temp.append(nums[start])
                    dfs(start + 1, nums, temp, res, n)
                    temp.pop()

        dfs(0, nums, temp, res, n)
        return res