# 超时
# class Solution:
#     def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
#         t_count, f_count = 0, 0
#         left, right = 0, 0
#         while True:
#             if right > len(answerKey):
#                 break
#             if max(answerKey[left:right].count('T'), answerKey[left:right].count('F')) + k < right - left:
#                 left += 1
#
#             right += 1
#         return right - left - 1

class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        t_count, f_count = 0, 0
        left, right = 0, 0
        while True:
            if right >= len(answerKey):
                break
            if answerKey[right] == 'T':
                t_count += 1
            else:
                f_count += 1
            if max(f_count, t_count) + k < right - left + 1:
                if answerKey[left] == 'T':
                    t_count -= 1
                else:
                    f_count -= 1
                left += 1

            right += 1
        return right - left

if __name__ == '__main__':
    s = Solution()
    res = s.maxConsecutiveAnswers("TFFT", 1)
    print(res)

