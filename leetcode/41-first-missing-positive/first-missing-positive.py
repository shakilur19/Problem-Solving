class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = [i for i in nums if i > 0]

        if len(nums) == 0:
            return 1
        mset = set(nums)
        nums = list(mset)
        nums.sort()
        for i in range (len(nums)):
            if i+1 != nums[i]:
                return i+1
        return nums[-1] + 1
        