# 贪心算法
# class Solution:
#     def jump(self, nums:list) -> int:
#         if len(nums) < 2: return 0
#         cur_max = 0
#         end = 0
#         res = 0
#         for i in range(len(nums)):
#             cur_max = max(cur_max, i + nums[i])
#             if end == i:
#                 res += 1
#                 end = cur_max
#                 if end >= len(nums) - 1:
#                     return res


class Solution:
    def jump(self, nums:list) -> int:
        res = 0
        end = 0
        cur_max = 0
        for i in range(len(nums)):
            cur_max = max(cur_max, i + nums[i])
            if i == end:
                res += 1
                end = cur_max
                if end >= len(nums) - 1:
                    return res



if __name__ == '__main__':
    s = Solution()
    res = s.jump([2, 3, 1, 1, 4])
    print(res)






