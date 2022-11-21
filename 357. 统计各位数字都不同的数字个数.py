NUM_CHOICES = [9,] + list(range(9, 0, -1))
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        res = product = 1
        for i in range(n):
            product *= NUM_CHOICES[i]
            res += product
        return res



if __name__ == '__main__':
    s = Solution()
    s.countNumbersWithUniqueDigits(n=3)









