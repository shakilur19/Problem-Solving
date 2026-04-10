class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sum = nums[0]
        next = nums[0]

        for i in range(1, len(nums)):
            if next + 1 == nums[i]:
                next += 1
                sum += next
            else:
                break
        if sum not in nums:
            return sum
        nums = sorted(nums)
        
        for i in nums:
            if sum == i:
                sum += 1
        return sum