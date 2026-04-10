class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pre = nums[0]
        if len(nums) == 1:
            if pre < target:
                return 1
            else:
                return 0

        for i in range(1, len(nums)):
            if nums[i] == target:
                return i
            elif target < nums[i]:
                if pre < target:
                    return i
                else:
                    return i - 1
            elif nums[i] > target:
                if pre < target:
                    return i
                else:
                    return i + 1
        return len(nums)
        