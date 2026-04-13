class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = [1]
        for i in range(rowIndex):
            row = [1] * (len(ans) + 1)
            for j in range(1, len(ans)):
                row[j] = ans[j-1] + ans[j]
            ans = row
        
        return ans