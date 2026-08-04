class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n_shifts = 0
        N = len(nums)

        for n in range(N):
            num = nums[n-n_shifts]

            if num == val:
                nums[n-n_shifts:-1] = nums[n-n_shifts+1:]
                n_shifts += 1
                
        return N - n_shifts

        