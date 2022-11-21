from typing import *
import copy


# 使用visited记录选过的数会得出全排列
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         visited = [False for _ in range(len(nums))]
#         path = []
#         temp = 0
#         res = []
#         nums.sort()
#
#         def dfs(temp, res, path):
#             if len(path) == 2:
#                 if temp == target:
#                     res.append(copy.deepcopy(path))
#                     return
#                 return
#
#             for i in range(len(nums)):
#                 if visited[i] == False:
#                     path.append(nums[i])
#                     temp += nums[i]
#                     visited[i] = True
#                     dfs(temp, res, path)
#                     temp -= nums[i]
#                     path.pop()
#                     visited[i] = False
#
#         dfs(temp, res, path)
#         return res

# dfs 超时
# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         path = []
#         temp = 0
#         res = []
#         nums.sort()
#
#         def dfs(temp, res, path, start):
#
#             if len(path) == 4:
#                 if temp == target:
#                     res.append(copy.deepcopy(path))
#                     return
#                 return
#
#             for i in range(start, len(nums)):
#                 # 去掉同一层选到相同的元素
#                 if i > start and nums[i] == nums[i - 1]:
#                     continue
#                 # 优化剪枝后不会超时
#                 if temp + (4 - len(path)) * nums[i] > target:
#                     continue
#
#                 if temp + nums[i] + (3 - len(path)) * nums[-1] < target:
#                     continue
#                 path.append(nums[i])
#                 temp += nums[i]
#                 dfs(temp, res, path, i + 1)
#                 temp -= nums[i]
#                 path.pop()
#
#         dfs(temp, res, path, 0)
#         return res

# 双指针
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = set()
        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                now = nums[i] + nums[j]
                p = j + 1
                q = len(nums) - 1
                while p < q:
                    if nums[p] + nums[q] + now == target:
                        if (nums[i], nums[j], nums[p], nums[q]) not in ans:
                            ans.add((nums[i], nums[j], nums[p], nums[q]))
                    if nums[p] + nums[q] + now > target:
                        q -= 1
                    else:
                        p += 1
        return list(ans)


if __name__ == '__main__':
    s = Solution()
    res = s.fourSum([1,0,-1,0,-2,2], 0)
    print(res)
