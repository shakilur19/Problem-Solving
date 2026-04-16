class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isDuplicate(arr):
            ans = []
            for i in range(9):
                if arr[i] !=0:
                    ans.append(arr[i])
            return len(ans) == len(set(ans))
        rows = []
        col = 0
        for i in range(9):
            r_l = []
            for j in range(9):
                r_l.append(board[i][j] if board[i][j] != "." else 0)
            rows.append(r_l)

        for i in range(9):
            if not isDuplicate(rows[i]):
                return False
        
        for i in range(9):
            col = [row[i] for row in rows] 
            if not isDuplicate(col):
                return False

        squire = []

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = []
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        box.append(board[i][j] if board[i][j] != "." else 0)
                squire.append(box)
        
        for i in range(9):
            if not isDuplicate(squire[i]):
                return False

        return True