import copy
class Solution:
    def permuteUnique(self, nums: list):
        res = []
        temp = []
        visited = [False for i in range(len(nums))]

        def dfs(nums, res, temp):
            if len(temp) == len(nums):
                if temp not in res:
                    res.append(copy.deepcopy(temp))
                return


            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    temp.append(nums[i])
                    dfs(nums, res, temp)
                    visited[i] = False
                    temp.pop()


        dfs(nums, res, temp)
        return res

if __name__ == '__main__':
    s = Solution()
    res = s.permuteUnique([1, 2, 3])
    print(list(res))








