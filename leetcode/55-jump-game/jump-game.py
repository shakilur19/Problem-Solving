class Solution:
    def canJump(self, nums: List[int]) -> bool:
        size = len(nums)

        if size == 1:
            return True
        if nums[0] == 0:
            return False

        maxDistance = 0

        for i in range(size):
            if i > maxDistance:
                return False

            tempVal = nums[i] + i
            if tempVal > maxDistance:
                maxDistance = tempVal

            if maxDistance >= size - 1:
                return True

        return False