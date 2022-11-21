from typing import *
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        temp = {}
        for i, j in enumerate(nums):
            temp[i] = temp.get(j, 0) + i




