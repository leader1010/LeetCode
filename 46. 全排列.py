# 给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。
# import copy
# class Solution(object):
#     def permute(self, nums: list):
#         visited = [False for _ in range(len(nums))]
#         res =[]
#         temp = []
#
#
#         def dfs(index, nums, temp, res):
#             if index == len(nums):
#                 res.append(copy.deepcopy(temp))
#                 return res
#
#
#             for i in range(len(nums)):
#                 if not visited[i]:
#                     temp.append(nums[i])
#                     visited[i] = True
#                     dfs(index + 1, nums, temp, res)
#                     visited[i] = False
#                     temp.pop()
#
#         dfs(0, nums, temp, res)

#   扩展3选二组合
# import copy
# class Solution(object):
#     def select(self, nums: list, n):
#         visited = [False for _ in range(len(nums))]
#         temp = []
#         res = []
#
#
#         def dfs(index, nums, temp, visited, res, n):
#             if index == n:
#                 res.append(copy.deepcopy(temp))
#                 return res
#
#             for i in range(0 + index, len(nums)):
#                 if not visited[i]:
#                     temp.append(nums[i])
#                     visited[i] = False
#                     dfs(index + 1, nums, temp, visited, res, n)
#                     visited[i] = True
#                     temp.pop()
#
#         dfs(0, nums, temp, visited, res, n)
#         return res

# 组合
import copy


class Solution(object):
    def select(self, nums: list, n):
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


if __name__ == '__main__':
    s = Solution()
    res = s.select([1, 2, 3, 4], 3)
    print(res)
