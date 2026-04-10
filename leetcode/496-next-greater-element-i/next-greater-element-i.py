class Solution:
    def findNext(self, index, num, value):
        for i in range(index, len(num)):
            if value < num[i]:
                return num[i]
        return -1
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        dict = {}
        for i in range(len(nums2) - 1):
            dict[nums2[i]] = self.findNext(i+1, nums2, nums2[i])

        dict[nums2[-1]] = -1

        for num in nums1:
            answer.append(dict[num])

        return answer