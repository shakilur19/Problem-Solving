class Solution:
    def doRob(self, nums: List[int]) -> int:
        size = len(nums)
        vct = []

        if size == 1:
            return nums[0]
        elif size == 2:
            return max(nums[0], nums[1])

        vct.append(nums[0])
        vct.append(max(nums[0], nums[1]))

        for i in range(2, size):
            findMax = max(nums[i] + vct[i - 2], vct[i - 1])
            vct.append(findMax)

        return vct[size - 1]

    def rob(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 1:
            return nums[0]

        v1 = []
        v2 = []

        for i in range(size):
            if i != 0:
                v1.append(nums[i])
            if i != size - 1:
                v2.append(nums[i])

        return max(self.doRob(v1), self.doRob(v2))