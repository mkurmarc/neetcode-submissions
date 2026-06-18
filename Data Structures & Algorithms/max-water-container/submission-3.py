class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxVolume = 0
        while left < right:
            currentVolume = min(heights[left], heights[right]) * (right - left)
            maxVolume = max(currentVolume, maxVolume)
            if heights[left] < heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
            else:
                left += 1
                right -= 1
        return maxVolume
