class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic : dict[int, int] = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                dic[nums[i]] += 1
            else:
                dic[nums[i]] = 1
            
        sorted_freq = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
        return list(sorted_freq.keys())[:k]



