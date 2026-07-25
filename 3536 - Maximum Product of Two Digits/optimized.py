class Solution:
    def maxProduct(self, n: int) -> int:
        str_num = str(n)
        nums = []
        for i, val in enumerate(str_num):
            nums.append(int(val))
        res = 0
        nums.sort()
        return nums[-1] * nums[-2]