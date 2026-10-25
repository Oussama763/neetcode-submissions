class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            current_container = (j - i)*min(heights[i], heights[j])
            container = current_container if current_container > container else container
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
            
        return container