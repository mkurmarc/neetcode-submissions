class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            # triplets consisting of only positive numbers will never equal 0
            if nums[i] > 0:
                break
            # to avoid duplicate triplets, skip 'a' if it's the same as the prev num
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # find all pairs that sum to a target of '-a' (-nums[i])
            pairs = self.pairSumSortedAllPairs(nums, i + 1, -nums[i])
            for pair in pairs:
                triplets.append([nums[i]] + pair)
        return triplets
            
    def pairSumSortedAllPairs(self, nums, start, target):
        pairs = []
        left, right = start, len(nums) - 1

        while left < right:
            pairSum = nums[left] + nums[right]
            if pairSum == target:
                pairs.append([ nums[left], nums[right] ])
                left +=1
                # to avoid duplicate '[b, c]' pairs, skip 'b' if it is the same as prev num
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif pairSum < target:
                left += 1
            else:
                right -= 1
        return pairs

            

# i + j + k = 0
# j + k = -i