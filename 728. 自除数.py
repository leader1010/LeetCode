class Solution:
    def selfDividingNumbers(self, left: int, right: int):
        set_range = [i for i in range(left, right)]
        res = []
        for i in set_range:
            for x in str(i):
                if x == "0":
                    break
                if i % int(x) == 0:
                    continue
                else:
                    break
            else:
                res.append(i)
        return res

# 参考除十  对十取余
# class Solution:
#     def selfDividingNumbers(self, left: int, right: int) -> List[int]:
#         def isSelfDividing(num: int) -> bool:
#             x = num
#             while x:
#                 x, d = divmod(x, 10)
#                 if d == 0 or num % d:
#                     return False
#             return True
#         return [i for i in range(left, right + 1) if isSelfDividing(i)]

