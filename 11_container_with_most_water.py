class Solution:

    # O(N^2) time limit
    def maxArea1(self, height: list[int]) -> int:
        max_water = 0
        len_height = len(height)
        
        for l in range(len_height-1):
            for r in range(l+1, len_height):
                max_water = max(max_water, (r-l) * min(height[l], height[r]))

        return max_water 

    # O(N) Two pointer
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        l, r = 0, len(height) - 1

        while l < r:
            water = min(height[l], height[r]) * (r - l)
            max_water = max(water, max_water)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return max_water
    