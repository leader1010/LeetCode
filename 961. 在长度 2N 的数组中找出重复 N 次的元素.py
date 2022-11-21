import collections

class Solution:
    def repeatedNTimes(self, nums) -> int:
        n = len(nums) // 2
        # a = len(set(nums))
        nums_dict = collections.defaultdict()
        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) +1
        for i in nums_dict:
            if nums_dict[i] == n:
                return i



if __name__ == '__main__':
    s = Solution()
    res = s.repeatedNTimes([1,2,3,3])

