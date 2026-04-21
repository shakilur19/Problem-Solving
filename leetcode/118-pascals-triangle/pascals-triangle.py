class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(1, numRows+1):
            temp = [1] * i
            for j in range(1, i-1):
                temp[j] = ans[i-2][j-1] + ans[i-2][j]
            ans.append(temp)

        return ans
