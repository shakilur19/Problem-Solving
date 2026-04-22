class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(path, open_count, close_count):
            if len(path) == (2 * n):
                ans.append(path)
                return

            if open_count < n:
                dfs(path + "(", open_count+1, close_count)
            if close_count < open_count:
                dfs(path + ")", open_count, close_count+1)
            
        dfs("", 0, 0)
        return ans
        