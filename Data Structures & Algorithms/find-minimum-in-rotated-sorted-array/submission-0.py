class Solution:
    def findMin(self, nums: List[int]) -> int:
        high = len(nums) - 1
        low = 0
        while low != high:
            mid = (high + low) // 2
            if nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[high]