class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        duplicates = set()
        
        for i in range(len(nums)):
            if nums[i] not in duplicates:
                duplicates.add(nums[i])
                seen = set()
                target = -nums[i]
                
                for j in range(i + 1, len(nums)):
                    complement = target - nums[j]
                    if complement in seen:
                        res.add(tuple(sorted((nums[i], nums[j], complement))))
                    seen.add(nums[j])
                    
        return [list(triplet) for triplet in res]