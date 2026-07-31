class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary of target minus number: index pairs
        dict_pairs = dict()

        for i, num in enumerate(nums):
            if num in dict_pairs.keys():
                return [dict_pairs[num], i]
            else:
                dict_pairs[target - num] = i
         
        