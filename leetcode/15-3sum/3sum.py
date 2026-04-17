class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            seen = set()
            for j in range(i + 1, len(nums)):
                third_number = -(nums[i] + nums[j])

                if third_number in seen:
                    ans.add((nums[i], third_number, nums[j]))

                seen.add(nums[j])

        return [list(x) for x in ans]