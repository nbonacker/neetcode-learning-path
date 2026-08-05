class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        thershold = int( n / 2)
        current_max = 0
        counts = dict()

        for num in nums:
            if num in counts:
                counts[num] += 1
                current_max = max(counts[num], current_max)
            else:
                counts[num] = 1
                current_max = max(1, current_max)
            if current_max > thershold:
                return num
