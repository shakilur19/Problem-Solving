class Solution(object):
    def removeDuplicates(self, nums):
        j = 1
        length = len(nums)
        for i in range(1, length):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j = j + 1
        return j
        