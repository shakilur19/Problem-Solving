class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)

        maxDistance = 0
        counter = 0
        track = 0

        for i in range(size - 1):
            tempVal = nums[i] + i
            maxDistance = max(maxDistance, tempVal)

            if i == track:
                counter += 1
                track = maxDistance

        return counter