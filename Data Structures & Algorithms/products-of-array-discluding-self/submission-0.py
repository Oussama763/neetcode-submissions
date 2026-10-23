class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = 1
        o_t = [1] * n
        for i in range(n):
            o_t[i] = s
            s *= nums[i]
        s = 1
        for j in range(n - 1, -1, -1):
            o_t[j] *= s
            s *= nums[j]
        return o_t
