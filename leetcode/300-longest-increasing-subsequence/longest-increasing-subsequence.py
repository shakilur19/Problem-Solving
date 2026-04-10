class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = []
        ans.append(nums[0])

        def remove_item(num: List[int], item: int) -> List[int]:
            for i in range(len(num)):
                if item <= num[i]:
                    print(num[i], item)
                    num[i] = item
                    break
            return num

        for i in range(1, len(nums)):
            if nums[i] > ans[-1]:
                ans.append(nums[i])
            else:
                ans = remove_item(ans, nums[i])
        return len(ans)