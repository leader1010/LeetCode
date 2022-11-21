class Solution:
    def buildArray(self, nums):
        return [nums[i] for i in nums]





if __name__ == '__main__':
    s = Solution()
    res = s.buildArray([0, 2, 3])
    print(res)
