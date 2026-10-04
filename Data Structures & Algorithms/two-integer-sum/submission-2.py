class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            if x in [num for j, num in enumerate(nums) if j != i]:
                return [i, nums.index(x, i+1, len(nums))]