class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mysetlen = len(set(nums))
        numlen = len(nums)
        return mysetlen != numlen
        