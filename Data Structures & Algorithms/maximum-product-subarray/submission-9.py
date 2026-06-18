class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        min_product, max_product = 1, 1

        for n in nums:
            tmp = max_product * n
            max_product = max(min_product * n, max_product * n, n)
            min_product = min(min_product * n, tmp, n)
            result = max(max_product, result)
        return result


