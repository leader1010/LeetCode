class Solution:
    def replaceElements(self, arr):
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break
            arr[i] = max(arr[i+1:])
        return arr

if __name__ == '__main__':
    s = Solution()
    res = s.replaceElements([17,18,5,4,6,1])
    print(res)