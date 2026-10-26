class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        water = 0

        i = 0
        j = n - 1

        max_i = height[i]
        max_j = height[j]

        while i < j:

            if height[i] < height[j]:
                max_i = max(max_i, height[i+1])
                water += max_i - height[i+1]
                i += 1

            else:
                max_j = max(max_j, height[j-1])
                water += max_j - height[j-1]
                j -= 1

        return water