class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Maps the required complement to its index
        complements = {}

        for i, num in enumerate(nums):
            if num in complements:
                return [complements[num], i]
            else:
                complements[target - num] = i