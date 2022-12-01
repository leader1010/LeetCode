from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        res_count = []
        num = 0
        for i in range(len(nums)):
            num += nums[i]
            res_count.append(num)
        self.res_count = res_count

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.res_count[right]
        else:
            return self.res_count[right] - self.res_count[left - 1]

# *****
# class NumArray:
#
#     def __init__(self, nums):
#         self.sums = [0]
#         for i in nums:
#             self.sums.append(self.sums[-1] + i)
#
#     def sumRange(self, left: int, right: int) -> int:
#         _sums = self.sums
#         return _sums[right + 1] - _sums[left]


if __name__ == '__main__':
    s = NumArray([-2, 0, 3, -5, 2, -1])
    print(s.sumRange(2, 5))
