import copy


# 会存在重复
# class Solution:
#     def threeSum(self, nums):
#         temp = []
#         res = []
#
#         def dfs(nums, temp, res, start):
#             if len(temp) == 3:
#                 if sum(temp) == 0:
#                     res.append(copy.deepcopy(temp))
#                 return
#
#
#             for start in range(start, len(nums)):
#                 temp.append(nums[start])
#                 dfs(nums, temp, res, start + 1)
#                 temp.pop()
#
#         dfs(nums, temp, res, 0)
#         return res


# 双指针求解
class Solution:
    def threeSum(self, nums):
        left = 0
        right = len(nums) - 1
        nums.sort()
        res = []

        for i in range(len(nums)):
            while True:
                if left >= right:
                    break
                t_sum = nums[right] + nums[left + 1 + i]
                if t_sum > 0 - nums[i]:
                    right -= 1
                elif t_sum < 0 - nums[i]:
                    left += 1
                else:
                    while True:
                        if nums[left + 1] == nums[left]:
                            left += 1
                        elif nums[right - 1] == nums[right]:
                            right -= 1
                        else:
                            break
                    res.append([nums[i], nums[left + 1 + i], nums[right]])
                    right -= 1
                    left += 1

        return res


if __name__ == '__main__':
    s = Solution()
    res = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(res)
