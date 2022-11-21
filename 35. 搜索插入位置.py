from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while True:
            if left > right:
                return left
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid

if __name__ == '__main__':
    s = Solution()
    res = s.searchInsert([1, 1, 3, 5, 6], 3)
    print(res)
