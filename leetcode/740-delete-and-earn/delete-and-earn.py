class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        size = len(nums)

        if size == 1:
            return nums[0]

        nums.sort(reverse=True)

        m = {}

        for num in nums:
            if num in m:
                m[num] += num
            else:
                m[num] = num

        vct = []

        for key, value in m.items():
            vct.append((key, value))

        vct.append((0, 0))
        vct.append((0, 0))

        vct.sort(key=lambda x: x[0], reverse=True)

        k1 = vct[0][0]
        k2 = vct[1][0]
        v1 = vct[0][1]
        v2 = vct[1][1]

        earn1 = vct[0][1]
        earn2 = max(v1, v2)

        if k1 - 1 != k2:
            earn2 = v1 + v2

        for i in range(2, len(vct) - 1):
            k1 = vct[i][0]
            k2 = vct[i - 1][0]
            v1 = vct[i][1]
            v2 = vct[i - 1][1]

            if k1 == k2 - 1:
                temp = earn2
                earn2 = max(earn1 + v1, earn2)
                earn1 = temp
            else:
                temp = earn2
                earn2 = v1 + earn2
                earn1 = temp

        return max(earn1, earn2)