class Solution:
    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1) % 2 == 0:
            left = len(nums1) // 2 - 1
            right = len(nums1) // 2
            return (nums1[left] + nums1[right]) / 2
        else:
            i = len(nums1) // 2 + 1
            return nums1[i - 1]


if __name__ == '__main__':
    s = Solution()
    s.findMedianSortedArrays(nums1=[1, 2], nums2=[3, 4])
