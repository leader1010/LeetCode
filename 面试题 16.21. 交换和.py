class Solution:
    def findSwapValues(self, array1, array2):
        left, right = 0, len(array1)
        sum1 = sum(array1)
        sum2 = sum(array2)
        if sum1 == sum2:
            return []
        if sum1 > sum2:
            for i in array2:
                







