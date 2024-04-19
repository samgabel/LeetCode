class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {}
        for i, num in enumerate(nums):
            # dictionary lookups using `in` are O(1) time
            if target - num in nums_idx:
                return [i, nums_idx[target - num]]
            nums_idx[num] = i