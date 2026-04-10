class Solution:
    def numberOfEmployeesWhoMetTarget(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] >= k:
                count += 1
            
        return count
        