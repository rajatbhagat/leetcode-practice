class Solution:
    def maxProduct(self, n: int) -> int:
        str_num = str(n)
        nums = []
        for i, val in enumerate(str_num):
            nums.append(int(val))
        res = 0
        i = 0
        j = 0
        while i < len(nums):
            if i == j:
                j += 1
                continue
            product = nums[i] * nums[j]
            res = res if res > product else product
            j += 1
            if j >= len(nums) - 1:
                j = 0
                i += 1
        return res
            