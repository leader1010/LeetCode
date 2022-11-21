from typing import List
import collections


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        cnt, l = len(words), len(words[0])
        i, j = 0, cnt * l - 1
        ans = []
        check = collections.Counter(words)
        while j < len(s):
            ss = s[i: j + 1]
            tmp = []
            for k in range(0, len(ss), l):
                tmp.append(ss[k: k + l])
            if collections.Counter(tmp) == check:
                ans.append(i)
            i += 1
            j += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    s.findSubstring(s="wordgoodgoodgoodbestword", words=["word","good","best","word"])