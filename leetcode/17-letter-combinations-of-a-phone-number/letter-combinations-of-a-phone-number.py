class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def getCom(pre, post):
            ans = []
            for i in range(len(pre)):
                if len(post) > 0:
                    for j in range(len(post)):
                        ans.append(post[j] + pre[i])
                else:
                    ans.append(pre[i])
            return ans

        com = []
        post = []
        for d in digits:
            post = getCom(map[d], post)
        return post
        