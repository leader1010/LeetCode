import collections
from typing import List


# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         sums = [0 for _ in range(len(nums) + 1)]
#         if len(nums) == 1:
#             if nums[0] == k:
#                 return 1
#             else:
#                 return 0
#
#         for i in range(len(nums)):
#             sums[i + 1] = nums[i] + sums[i]
#         self.count = 0
#
#         count = 0
#         for i in range(1, len(sums)):
#             for j in range(i):
#                 if sums[j] == sums[i] - k:
#                     count += 1
#         # 超时**************************************
#         # for i in range(len(sums) - 1, -1, -1):
#         #
#         #     count += sums[:i].count(sums[i] - k)
#         #     if k == sums[i]:
#         #         count += 1
#
#         # 超时
#         # res = 0
#         # def dfs(sums, index, target):
#         #     if index >= len(sums):
#         #         return
#         #     if sums[index] == target:
#         #         self.count += 1
#         #     dfs(sums, index + 1, target)
#
#         # for i in range(len(sums)):
#         #     dfs(sums[i + 1:], 0, target=sums[i] + k)
#         #     if sums[i] == k:
#         #         res += 1
#         return count


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 要求的连续子数组
        count = 0
        n = len(nums)
        preSums = collections.defaultdict(int)
        preSums[0] = 1

        presum = 0
        for i in range(n):
            presum += nums[i]

            # if preSums[presum - k] != 0:
            count += preSums[presum - k]  # 利用defaultdict的特性，当presum-k不存在时，返回的是0。这样避免了判断

            preSums[presum] += 1  # 给前缀和为presum的个数加1

        return count


if __name__ == '__main__':
    s = Solution()
    res = s.subarraySum([1, 1, 1], 1)
    print(res)
