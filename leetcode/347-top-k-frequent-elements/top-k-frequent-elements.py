class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans_map = {}

        for num in nums:
            if num in ans_map:
                ans_map[num] = ans_map[num] + 1
            else:
                ans_map[num] = 1

        s_map = sorted(ans_map.items(), key=lambda item: item[1], reverse=True)

        ans = []
        i = 0
        for key, value in s_map:
            if i < k:
                ans.append(key)
                i += 1

        return ans