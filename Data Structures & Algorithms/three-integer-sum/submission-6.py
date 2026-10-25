class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        # Find all duplicates, we only need to process unique starting points
        duplicates = set()
        
        for i in range(len(nums)):
            if nums[i] not in duplicates:
                duplicates.add(nums[i])
                
                # This set tracks numbers we've seen so far in the inner loop
                seen = set()
                target = -nums[i]
                
                for j in range(i + 1, len(nums)):
                    complement = target - nums[j]
                    
                    # O(1) lookup, and 'seen' is built gradually, not from a slice
                    if complement in seen:
                        # Found a triplet! Sort it to avoid duplicates in the final result
                        res.add(tuple(sorted((nums[i], nums[j], complement))))
                    
                    # Add current number to seen for future lookups
                    seen.add(nums[j])
                    
        return [list(triplet) for triplet in res]