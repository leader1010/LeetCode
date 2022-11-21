class Solution:
    def findDifferentBinaryString(self, nums) -> str:
        length = len(nums)
        path = ['0', '1']
        temp = ''
        res = []

        def dfs(nums, temp, path, res):
            if len(temp) == len(nums):
                if temp in nums:
                    return
                res.append(temp)
                return
            for i in range(len(path)):
                temp += path[i]
                dfs(nums, temp, path, res)
                if res:
                    break
                temp = temp[:-1]


        dfs(nums, temp, path, res)
        return res[0]

if __name__ == '__main__':
    s = Solution()
    res = s.findDifferentBinaryString(["00","01"])
    print(res)


