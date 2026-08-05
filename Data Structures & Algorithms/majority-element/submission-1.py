class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        thershold = int( n / 2)
        counts = dict()

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > thershold:
                return num
