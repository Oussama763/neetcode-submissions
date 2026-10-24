class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_length = 0
        #len_dict : dict[str, List[int]]
        for i in range(len(nums)):
            current_max = 0
            if nums[i] - 1 not in nums_set:
                j = 0
                while nums[i] + j in nums_set:
                    current_max += 1
                    j += 1
                max_length = current_max if current_max > max_length else max_length
        return max_length