class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        ans = []
        for arr in points:
            distance = pow(abs(arr[0]),2) + pow(abs(arr[1]),2)
            ans.append((distance, arr))

        ans.sort()
        picked = []
        for item in ans[:k]:
            picked.append(item[1])
        return picked