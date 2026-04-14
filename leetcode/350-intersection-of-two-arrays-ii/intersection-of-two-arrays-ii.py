class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}

        for i in nums1:
            mp[i] = mp.get(i, 0) + 1

        ans = []

        for i in nums2:
            if i in mp and mp[i] > 0:
                ans.append(i)
                mp[i] -= 1

        return ans