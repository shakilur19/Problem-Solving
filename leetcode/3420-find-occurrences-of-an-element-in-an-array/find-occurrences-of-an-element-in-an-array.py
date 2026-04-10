class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        arr = []
        for idx, val in enumerate(nums):
            if val == x:
                arr.append(idx)

        print(arr)
        occurrences = []
        max_occurrence = len(arr)
        i = 0

        for idx, val in enumerate(queries):
            if val <= max_occurrence:
                occurrences.append(arr[val - 1])
                i +=1
            else:
                occurrences.append(-1)

        return occurrences
        