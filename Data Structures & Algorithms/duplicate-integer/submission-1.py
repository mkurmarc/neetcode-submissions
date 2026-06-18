class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        all_nums = set()
        for num in nums:
            if num in all_nums:
                return True
            all_nums.add(num)  
        return False   