import copy
class Solution:
    def largestDivisibleSubset(self, nums: list):
        nums.sort()
        if not nums:
            return
        res = []
        temp = []

        def dfs(start, nums:list, temp:list, res):
            for i in range(start ,len(nums)):
                # if 0 == len(nums):
                #     res = temp if len(temp) > len(res) else res
                #     return res
                # if len(temp) == 1 and nums[i] % temp[0] == 0:
                #     temp.append(nums[i])
                # elif len(temp) == 0:
                #     temp.append(nums[i])
                # dfs(start + 1, nums, temp, res)
                # temp.pop()
                dfs(start + 1, nums, temp, res)




        dfs(0, nums, temp, res)
        return res


if __name__ == '__main__':
    s = Solution()
    s.largestDivisibleSubset([1, 2, 3])














