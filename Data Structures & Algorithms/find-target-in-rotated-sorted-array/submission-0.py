class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_inflection(nums):
            lo, hi = 0, len(nums) - 1
            while hi != lo:
                mid = (lo + hi) // 2
                if nums[mid] < nums[hi]:
                    hi = mid
                else:
                    lo = mid + 1
            return hi #index

        def binary_search(nums, lo, hi):
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    return mid # value
            return -1


        min_index = find_inflection(nums)
        left_side = binary_search(nums, 0, min_index - 1)
        right_side = binary_search(nums, min_index, len(nums) - 1)
        if left_side == -1 and right_side == -1:
            return -1
        elif left_side != -1:
            return left_side
        else:
            return right_side