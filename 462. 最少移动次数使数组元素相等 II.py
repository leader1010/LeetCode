class Solution:
    def minMoves2(self, nums: list) -> int:
        nums.sort(reverse=True)
        target = len(nums) // 2
        res = 0
        for k in range(len(nums)):
            res += abs(nums[target] - nums[k])
        return res
